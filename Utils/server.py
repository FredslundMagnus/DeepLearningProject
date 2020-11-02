
from Utils.debug import checkServer, getvals, profilingStats, showParams
import pickle

isServer = checkServer()

defaults = {
    'name': "Agent",
    'lossf': 'MME',
    'discount': 0.9,
    'lambd': 0.9,
    'lr': 0.001,
    'dropout': 0,
}

params = getvals(defaults) if isServer else None


def serverRun():
    showParams()
    profilingStats()


def saveAgent(agent, name: str):
    pickle.dump(agent, open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.obj", "wb"))
