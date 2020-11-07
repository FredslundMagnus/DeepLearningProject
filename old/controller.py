from agent import Agent
from environments import Environment
import torch
import multiprocessing
from multiprocessing import Pool
import os
from helpers import clean
import time
from Utils.debug import disablePrint, enablePrint
import pickle
from os import listdir
from os.path import isfile, join

device = torch.device('cpu')
hidden_size = 100


def saveData(agent: Agent, location: str, ID: int):
    memory = agent.memory.memory
    with open(f"{location}/Data/Player{ID}.data", "wb") as file:
        pickle.dump(memory, file)


def collectData(info):
    i, location, ID = info
    print('Start', ID)
    disablePrint()
    agent = Agent(memory=i)
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
    saveData(agent, location, ID)
    enablePrint()
    print('Done', ID)
    return os.getpid()


def trainAgent(frames, CPUs, location):
    agent = Agent(memory=frames * CPUs)
    fileNames = []
    while len(fileNames) != CPUs:
        fileNames = [f"{location}/Data/{f}" for f in listdir(f"{location}/Data/") if isfile(f"{location}/Data/{f}")]
    t0 = time.time()
    memory = []
    space = {0}
    while 0 in space:
        space = {os.path.getsize(file) for file in fileNames}
        print(".", end="")
    for fileName in fileNames:
        with open(fileName, 'rb') as file:
            memory += pickle.load(file)
        os.remove(fileName)
    for mem in memory:
        agent.remember(*mem)
    total = time.time() - t0
    print('Memory:', len(agent.memory), 'Time', total)
    print("Dones")
    a = os.getpid()
    print(a)
    return a


CPU = multiprocessing.cpu_count() - 1
if __name__ == "__main__":
    print('Start with number of CPUs:', CPU)
    t0 = time.time()
    frames = 10000
    location = 'trainlocally/multi'
    with Pool(processes=CPU) as pool:
        # res = pool.apply_async(trainAgent, args=(frames, CPU - 1, location))
        used_cpus = pool.map(collectData, [(frames, location, i) for i in range(CPU)])
        print('Used CPUs:', used_cpus)
        # print(res.get())
    total = time.time() - t0
    print('Done')
    print('Time', total)
    print('Frames pr. sekond:', frames * CPU / total)
