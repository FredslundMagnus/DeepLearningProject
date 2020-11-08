from environments import Environments
from Utils.server import isServer, params, serverRun, saveAgent, saveMean
from agent import Agent
from display_input import displayer
from Utils.debug import disablePrint
from time import time

if isServer:
    name, discount, environment, hours, memory, update_every, use_distribution = params
    print(*params)

    # the server runs the main function (can be changed)
    def main():
        agent = Agent(memory=memory, discount=discount)
        env = Environments(render=False, envs=[environment for _ in range(20)])
        dones, total_rew, f, all_return, tid = 0, 0, 0, [], time() + 3600 * hours - 100
        while time() < tid:
            f += 1
            obs, hn, cn = env.start()
            act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
            obs, rew, done, info = env.step(act, hn, cn)
            total_rew += sum(rew) / len(rew)
            dones += sum(done) / len(done)
            agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)
            if f > update_every:
                for _ in range(3):
                    agent.learn(double=True, use_distribution=use_distribution)
            if f % update_every == 0:
                agent.update_target_network()
                all_return.append(total_rew / dones)
                dones, total_rew = 0, 0
        saveAgent(agent, name)
        saveMean(all_return, name)
    serverRun()
else:
    agent = Agent()
    env = Environments(render=True, envs=['fruitbot' for _ in range(20)])
    all_return, all_dones = [], []
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
        if f > update_every:
            for _ in range(2):
                agent.learn(double=True)
        if f % update_every == 0:
            agent.update_target_network()
            all_dones.append(update_every/(dones+10**(-10)))
            all_return.append(total_rew/(dones+10**(-10)))
            dones, total_rew = 0, 0
        if f % (5 * update_every) == 0:
            displayer(obs[0].cpu(), agent, all_return, all_dones)
