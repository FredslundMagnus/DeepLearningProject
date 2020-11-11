from environments import Environments
from Utils.server import isServer, params, serverRun, saveAgent, saveMean
from agent import Agent
from display_input import displayer
from Utils.debug import disablePrint
from time import time

if isServer:
    name, discount, environment, hours, memory, update_every, use_distribution, double = params
    print(*params)

    # the server runs the main function (can be changed)
    def main():
        agent = Agent(memory=memory, discount=discount)
        env = Environments(render=False, envs=[environment for _ in range(20)])
        dones, total_rew, f, all_return, tid = 0, 0, 0, [], time() + 3600 * hours - 300
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
                    agent.learn(double=double, use_distribution=use_distribution)
            if f % update_every == 0:
                agent.update_target_network()
                all_return.append(total_rew / dones)
                dones, total_rew = 0, 0
        saveAgent(agent, name)
        saveMean(all_return, name)
    serverRun()
else:
    total_agents = 20
    update_every = 200
    calculate_every, display_every = 50, 10000
    # disablePrint()
    frames = 1000000
    all_return, all_dones = [], []
    dones, total_rew, k = 0, 0, 0

    agent = Agent()
    env = Environments(render=True, envs=['bigfish' for _ in range(total_agents)])
    for f in range(1, frames + 1):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
        obs, rew, done, info = env.step(act, hn, cn)
        total_rew += sum(rew) / len(rew)
        dones += sum(done) / len(done)
        agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)

        if f % update_every == 0:
            agent.update_target_network()
        if f > update_every:
            for _ in range(1):
                agent.learn(double=True)

        if (f + 1) % calculate_every == 0:
            k += 1
            if dones != 0:
                all_dones.append(k * calculate_every / dones)
                all_return.append(total_rew / dones)
                dones, total_rew, k = 0, 0, 0
        if f % display_every == 0:
            displayer(obs[0].cpu(), agent, all_return, all_dones, names="seen frames in " + str(total_agents * calculate_every) + "'s")
