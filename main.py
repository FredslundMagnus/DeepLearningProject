from environments import Environment, Environments
from Utils.server import isServer, params, serverRun, saveAgent, saveMean
from agent import Agent
from helpers import clean, hidden_size, device
import torch
from display_input import displayer
from runningList import RunningList
from Utils.debug import enablePrint, disablePrint
from time import time

if isServer:
    name, discount, environment, hours, memory, update_every = params
    print(*params)

    # the server runs the main function (can be changed)
    def main():
        agent = Agent(memory=memory, discount=discount)
        env = Environments(render=False, envs=[environment for _ in range(20)])
        dones, total_rew, f, all_return, t0 = 0, 0, 0, [], time()
        while time() - t0 < 3600 * hours - 100:
            f += 1
            obs, hn, cn = env.start()
            act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
            obs, rew, done, info = env.step(act, hn, cn)
            total_rew += sum(rew) / len(rew)
            dones += sum(done) / len(done)
            agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)
            if f > update_every:
                for _ in range(3):
                    agent.learn(double=True)
            if f % update_every == 0:
                agent.update_target_network()
                all_return.append(total_rew / dones)
                dones, total_rew = 0, 0
            saveAgent(agent, name)
            saveMean(all_return, name)
        serverRun()
else:
    # agent = Agent()
    # env = Environment(render=True).fruitbot  # env = Environment(render=True)["coinrun"]
    # start_learning = 0
    # update_every = 500
    # all_return = []
    # for i in range(20000):
    #     obs = clean(env.reset())
    #     hn = torch.zeros(1, 1, hidden_size, device=device)
    #     cn = torch.zeros(1, 1, hidden_size, device=device)
    #     total_rew = 0
    #     # print(torch.cuda.memory_allocated())
    #     while True:
    #         start_learning += 1
    #         # hn, cn = hn.detach(), cn.detach()
    #         act, obs_old, h0, c0, hn, cn = agent.choose(obs.to(device), hn, cn)  # env.action_space.sample()
    #         obs, rew, done, info = env.step(act)
    #         obs = agent.remember(obs_old.detach().cpu(), act, clean(obs).detach().cpu(), rew, h0.detach().cpu(), c0.detach().cpu(), hn.detach().cpu(), cn.detach().cpu(), int(not done))
    #         if start_learning > update_every:
    #             agent.learn(double=True)
    #         if start_learning % update_every == 0:
    #             agent.update_target_network()
    #         # if start_learning % (10 * update_every) == 0:
    #             # displayer(obs, agent, all_return)
    #         env.render()
    #         total_rew += rew
    #         if done:
    #             all_return.append(total_rew)
    #             print(f"\n{i}. Total reward: {total_rew}")
    #             # print(len(agent.memory))
    #             break
    #     env.close()
    agent = Agent()
    env = Environments(render=True, envs=['chaser' for _ in range(20)])
    all_return = []
    update_every = 100
    disablePrint()
    frames = 1000000
    dones, total_rew = 0, 0
    for f in range(1, frames + 1):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
        obs, rew, done, info = env.step(act, hn, cn)
        total_rew += sum(rew) / len(rew)
        dones += sum(done) / len(done)
        agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)
        enablePrint()
        print(torch.cuda.max_memory_allocated())
        disablePrint()
        if f > update_every:
            for _ in range(3):
                agent.learn(double=True)
        if f % update_every == 0:
            agent.update_target_network()
            all_return.append(total_rew / dones)
            dones, total_rew = 0, 0
        if f % (10 * update_every) == 0:
            displayer(obs[0].cpu(), agent, all_return)
