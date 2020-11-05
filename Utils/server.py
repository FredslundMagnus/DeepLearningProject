
from Utils.debug import checkServer, getvals, profilingStats, showParams
import pickle
from agent import Agent
isServer = checkServer()

defaults = {
    'name': "Agent",
    'discount': 0.99,
    'environment': 'fruitbot',
    'frames': 1000000,
    'memory': 100000
}

params = getvals(defaults) if isServer else None


def serverRun():
    showParams()
    profilingStats()


def saveAgent(agent: Agent, name: str, server=True):
    agent.memory.reset(0)
    agent.memory = None
    agent.remember = None
    if server:
        pickle.dump(agent, open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.obj", "wb"))
    else:
        pickle.dump(agent, open(f"trainlocally/{'-'.join(name.split('-')[:-1])}/{name}", "wb"))
