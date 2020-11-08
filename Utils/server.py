
from Utils.debug import checkServer, getvals, profilingStats, showParams
import pickle
from agent import Agent
from typing import List
isServer = checkServer()

defaults = {
    'name': "Agent",
    'discount': 0.999,
    'environment': 'fruitbot',
    'hours': 23,
    'memory': 200000,
    'update_every': 100,
    'use_distribution': 1,
    'double': 1,
}

params = getvals(defaults) if isServer else None


def serverRun():
    showParams()
    profilingStats()


def saveAgent(agent: Agent, name: str):
    agent.memory.reset(0)
    agent.memory = None
    agent.remember = None
    if isServer:
        pickle.dump(agent, open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.agent", "wb"))
    else:
        pickle.dump(agent, open(f"trainlocally/{'-'.join(name.split('-')[:-1])}/{name}", "wb"))


def saveMean(mean: List[float], name: str):
    if isServer:
        pickle.dump(mean, open(f"outputs/{'-'.join(name.split('-')[:-1])}/Means/{name}.means", "wb"))
    else:
        pickle.dump(mean, open(f"trainlocally/{'-'.join(name.split('-')[:-1])}/mean_{name}", "wb"))
