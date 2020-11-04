from environments import Environment
from Utils.server import isServer, params, serverRun, saveAgent
from agent import Agent
from helpers import clean, hidden_size, device
import torch
from display_input import displayer

if isServer:
    name, lossf, discount, lambd, lr, dropout = params
    print(name, lossf, discount, lambd, lr, dropout)

    # the server runs the main function (can be changed)
    def main():
        agent = Agent()
        env = Environment(render=False).bigfish  # env = Environment(render=True)["coinrun"]
        start_learning = 0
        update_every = 5000
        for i in range(10000):
            obs = clean(env.reset())
            hn = torch.zeros(2, 1, hidden_size, device=device)
            cn = torch.zeros(2, 1, hidden_size, device=device)
            total_rew = 0
            # print(torch.cuda.memory_allocated())
            while True:
                start_learning += 1
                # hn, cn = hn.detach(), cn.detach()
                act, obs_old, h0, c0, hn, cn = agent.choose(obs.to(device), hn, cn)  # env.action_space.sample()
                obs, rew, done, info = env.step(act)
                obs = agent.remember(obs_old.detach().cpu(), act, clean(obs).detach().cpu(), rew, h0.detach().cpu(), c0.detach().cpu(), hn.detach().cpu(), cn.detach().cpu(), int(not done))
                if start_learning > update_every:
                    agent.learn(double=True)
                if start_learning % update_every == 0:
                    agent.update_target_network()

                env.render()
                total_rew += rew
                if done:
                    print(f"\n{i}. Total reward: {int(total_rew)}")
                    # print(len(agent.memory))
                    break
            env.close()
        saveAgent(agent, name)
    serverRun()
else:
    agent = Agent()
    env = Environment(render=True).fruitbot  # env = Environment(render=True)["coinrun"]
    start_learning = 0
    update_every = 5000
    for i in range(20000):
        obs = clean(env.reset())
        hn = torch.zeros(2, 1, hidden_size, device=device)
        cn = torch.zeros(2, 1, hidden_size, device=device)
        total_rew = 0
        # print(torch.cuda.memory_allocated())
        while True:
            start_learning += 1
            # hn, cn = hn.detach(), cn.detach()
            act, obs_old, h0, c0, hn, cn = agent.choose(obs.to(device), hn, cn)  # env.action_space.sample()
            obs, rew, done, info = env.step(act)
            obs = agent.remember(obs_old.detach().cpu(), act, clean(obs).detach().cpu(), rew, h0.detach().cpu(), c0.detach().cpu(), hn.detach().cpu(), cn.detach().cpu(), int(not done))
            if start_learning > update_every:
                agent.learn(double=True)
            if start_learning % update_every == 0:
                agent.update_target_network()
                displayer(obs, agent)
                # saveAgent(agent, "trained", server=False)
            env.render()
            total_rew += rew
            if done:
                print(f"\n{i}. Total reward: {total_rew}")
                # print(len(agent.memory))
                break
        env.close()
