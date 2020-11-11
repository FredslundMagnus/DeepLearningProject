from collector import Collector
from environments import Environments
from Utils.server import isServer, params, serverRun, saveAgent, saveCollector
from agent import Agent
from display_input import displayer
from Utils.debug import disablePrint
from time import time

if isServer:
    name, discount, environment, hours, memory, update_every, use_distribution, double, total_agents, calculate_every, uncertainty = params
    print(*params)

    # the server runs the main function (can be changed)
    def main():
        agent = Agent(memory=memory, discount=discount, uncertainty=uncertainty, update_every=update_every, double=double, use_distribution=use_distribution)
        env = Environments(render=False, envs=[environment for _ in range(total_agents)])
        collector = Collector(calculate_every=calculate_every, total_agents=total_agents)
        tid = time() + 3600 * hours - 300
        while time() < tid:
            obs, hn, cn = env.start()
            act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
            obs, rew, done, info = env.step(act, hn, cn)
            collector.collect(rew, done, act)
            agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)
            agent.learn()
        saveAgent(agent, name)
        saveCollector(collector, name)
    serverRun()
else:
    total_agents, display_every = 20, 10000
    agent = Agent(discount=0.999, uncertainty=False, update_every=200, double=True, use_distribution=True)
    env = Environments(render=True, envs=['bigfish' for _ in range(total_agents)])
    collector = Collector(calculate_every=50, total_agents=total_agents)
    for f in range(1, 10000000):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
        obs, rew, done, info = env.step(act, hn, cn)
        collector.collect(rew, done, act)
        agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)
        agent.learn()

        if f % display_every == 0:
            displayer(obs[0].cpu(), agent, collector)
