from agent import Agent
from environments import Environment
import torch
from typing import List
import multiprocessing
from multiprocessing import Pool
import os
from helpers import clean
import time
from Utils.debug import enablePrint, disablePrint
device = torch.device('cpu')
hidden_size = 100


class Controllor:
    def __init__(self, environments: List[str], agents: List[Agent]) -> None:
        self.environments = environments
        self.agents = agents


def f(x):
    disablePrint()
    agent = Agent()
    env = Environment(render=False).fruitbot  # env = Environment(render=True)["coinrun"]
    start_learning = 0
    update_every = 5000
    for i in range(200):
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
            # if start_learning > update_every:
            #     agent.learn(double=True)
            if start_learning % update_every == 0:
                agent.update_target_network()
                # displayer(obs, agent)
                # saveAgent(agent, "trained", server=False)
            env.render()
            total_rew += rew
            if done:
                print(f"\n{i}. Total reward: {total_rew}")
                # print(len(agent.memory))
                break
        env.close()
    enablePrint()
    return os.getpid()


CPU = multiprocessing.cpu_count()
if __name__ == "__main__":
    print('Start')
    t0 = time.time()
    with Pool(processes=CPU) as pool:
        print(pool.map(f, range(CPU)))
    total = time.time() - t0
    print('Done', os.getpid())
    print('Time', total)
