
from Utils.debug import checkServer, getvals, profilingStats, showParams
import pickle
from typing import List
isServer = checkServer()

defaults = {
    'name': "Agent",
    'discount': 0.995,
    'environment': 'bigfish',
    'hours': 18,
    'memory': 500000,
    'update_every': 1000,
    'use_distribution': 1,
    'double': 1,
    'total_agents': 20,
    'calculate_every': 1000,
    'uncertainty': 1,
    'reward_normalization': 0,
    'exploration': 'epsilonGreedy',
    'hidden_size': 40,
    'uncertainty_weight': 0.1,
    'state_difference': 0,
    'state_difference_weight': 0.0,
}

params = getvals(defaults) if isServer else None


def serverRun():
    showParams(params)
    profilingStats()


def saveAgent(agent, name: str):
    agent.memory.reset(0)
    agent.memory = None
    agent.remember = None
    if isServer:
        pickle.dump(agent, open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.agent", "wb"))
    else:
        pickle.dump(agent, open(f"trainlocally/{'-'.join(name.split('-')[:-1])}/{name}", "wb"))


def saveCollector(collector, name: str):
    if isServer:
        pickle.dump(collector, open(f"outputs/{'-'.join(name.split('-')[:-1])}/Collectors/{name}.collect", "wb"))
    else:
        pickle.dump(collector, open(f"trainlocally/{'-'.join(name.split('-')[:-1])}/collect_{name}", "wb"))
