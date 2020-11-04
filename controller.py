from agent import Agent
from environments import Environment
import torch
import multiprocessing
from multiprocessing import Pool
import os
from helpers import clean
import time
from Utils.debug import disablePrint
device = torch.device('cpu')
hidden_size = 100


def f(i):
    disablePrint()
    agent = Agent(memory=i)
    env = Environment(render=False).fruitbot
    n = 0
    while i > 0:
        obs = clean(env.reset())
        hn = torch.zeros(2, 1, hidden_size, device=device)
        cn = torch.zeros(2, 1, hidden_size, device=device)
        while i > 0:
            i -= 1
            # hn, cn = hn.detach(), cn.detach()
            act, obs_old, h0, c0, hn, cn = agent.choose(obs, hn, cn)
            obs, rew, done, _ = env.step(act)
            obs = agent.remember(obs_old.detach(), act, clean(obs).detach(), rew, h0.detach(), c0.detach(), hn.detach(), cn.detach(), int(not done))
            env.render()
            if done:
                n += 1
                break
        env.close()
    return os.getpid()


CPU = multiprocessing.cpu_count()
if __name__ == "__main__":
    print('Start with number of CPUs:', CPU)
    t0 = time.time()
    frames = 10000
    with Pool(processes=CPU) as pool:
        res = pool.apply_async(f, [10])
        print(res.get(timeout=40))
        used_cpus = pool.map(f, [frames] * CPU * 2)
        print('Used CPUs:', used_cpus)
    total = time.time() - t0
    print('Done')
    print('Time', total)
    print('Frames pr. sekond:', frames * CPU / total)
