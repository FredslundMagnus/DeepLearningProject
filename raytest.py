import numpy as np
import psutil
import ray
import scipy.signal
from Utils.debug import enablePrint, disablePrint
from agent import Agent
from environments import Environment
import torch
from helpers import clean
import time

device = torch.device('cpu')
hidden_size = 100

num_cpus = psutil.cpu_count(logical=False)

ray.init(num_cpus=num_cpus)


@ray.remote
def f(image, random_filter):
    # Do some image processing.
    return scipy.signal.convolve2d(image, random_filter)[::5, ::5]


@ray.remote
def collectData(agent):
    print('Start', agent.memory.size)
    disablePrint()
    i = agent.memory.size
    env = Environment(render=False).fruitbot
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
                break
        env.close()
    enablePrint()
    print('Done')
    return agent.memory.memory

# Time the code below.


CPU = num_cpus
for _ in range(1):

    print('Start with number of CPUs:', CPU)
    t0 = time.time()
    frames = 5000
    location = 'trainlocally/multi'
    agent = ray.put(Agent(memory=frames))
    ray.get([collectData.remote(agent) for _ in range(num_cpus)])
    total = time.time() - t0
    print('Done')
    print('Time', total)
    print('Frames pr. sekond:', frames * CPU / total)
