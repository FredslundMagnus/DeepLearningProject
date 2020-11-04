from agent import Agent
from environments import Environment
import torch
import multiprocessing
from multiprocessing import Pool
import os
from helpers import clean
import time
from Utils.debug import enablePrint, disablePrint
device = torch.device('cpu')
hidden_size = 100


def f(i):
    disablePrint()
    agent = Agent()
    env = Environment(render=False).fruitbot
    while i > 0:
        obs = clean(env.reset())
        hn = torch.zeros(2, 1, hidden_size, device=device)
        cn = torch.zeros(2, 1, hidden_size, device=device)
        while True:
            # hn, cn = hn.detach(), cn.detach()
            act, obs_old, h0, c0, hn, cn = agent.choose(obs.to(device), hn, cn)
            obs, rew, done, info = env.step(act)
            obs = agent.remember(obs_old.detach().cpu(), act, clean(obs).detach().cpu(), rew, h0.detach().cpu(), c0.detach().cpu(), hn.detach().cpu(), cn.detach().cpu(), int(not done))
            env.render()
            if done:
                break
        env.close()
        i -= 1
    enablePrint()
    return os.getpid()


CPU = multiprocessing.cpu_count()
if __name__ == "__main__":
    print('Start', CPU)
    t0 = time.time()
    with Pool(processes=CPU) as pool:
        print(pool.map(f, [10000] * CPU))
    total = time.time() - t0
    print('Done', os.getpid())
    print('Time', total)
