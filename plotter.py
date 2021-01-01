import numpy as np
import matplotlib.pyplot as plt
import pickle


def returnplot(environment: str):
    plt.figure(figsize=(3.2, 2.3), dpi=200)
    collectorV1 = pickle.load(open(f"outputs/Base_{environment}/Collectors/Base_{environment}-0.collect", "rb"))
    collectorV2 = pickle.load(open(f"outputs/Base_v2_{environment}/Collectors/Base_v2_{environment}-0.collect", "rb"))
    collectorNOPE = pickle.load(open(f"outputs/NOPE_final_{environment}/Collectors/NOPE_final_{environment}-0.collect", "rb"))

    y1 = getData(collectorV1.all_return)
    y2 = getData(collectorV2.all_return)
    y3 = getData(collectorNOPE.all_return, k=50)

    plotOne(plt, y3, 'NOPE', k=50)
    plotOne(plt, y2, 'Base 2')
    plotOne(plt, y1, 'Base 1')

    plt.title(environment.capitalize())
    plt.legend(loc='lower right')
    plt.savefig(f'plots/{environment}.png')


def getData(returns, k=100):
    runnings = [0] * len(returns)
    for i in range(1, len(runnings) + 1):
        if i < k:
            runnings[i - 1] = sum(returns[:i]) / i
        else:
            runnings[i - 1] = sum(returns[(i - k):i]) / k
    return runnings


def plotOne(plt, y, label, k=100):
    plt.plot([a / k for a in range(len(y))], y, label=label)


environments = ['bigfish', 'bossfight', 'caveflyer', 'chaser', 'climber', 'coinrun', 'dodgeball', 'fruitbot', 'heist', 'jumper', 'leaper', 'maze', 'miner', 'ninja', 'plunder', 'starpilot']
for env in environments:
    returnplot(env)
