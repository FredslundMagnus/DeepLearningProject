import pickle
from environments import Environments
from Utils.debug import disablePrint, enablePrint


def evaluate(name, environment, n=0):
    disablePrint()
    name = name + '-' + str(n)
    agent = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.agent", "rb"))
    agent.explore = agent.exploration.greedy
    agent.uncertainty = False
    agent.state_avoidance = False
    env = Environments(render=False, envs=[environment for _ in range(20)], agent=agent)
    rews, dones = [], []
    for i in range(20000):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
        obs, rew, done, info = env.step(act, hn, cn)
        rews.append(sum(rew))
        dones.append(sum(done))
    enablePrint()
    score = sum(rews) / sum(dones)
    print(name.ljust(20, ' '), int(100 * (score - rMin[environment]) / (rMax[environment] - rMin[environment])) / 100, "  ", score)


rMin = {
    'bigfish': 1,
    'bossfight': 0.5,
    'caveflyer': 3.5,
    'chaser': 0.5,
    'climber': 2,
    'coinrun': 5,
    'dodgeball': 1.5,
    'fruitbot': -1.5,
    'heist': 3.5,
    'jumper': 3,
    'leaper': 3,
    'maze': 5,
    'miner': 1.5,
    'ninja': 3.5,
    'plunder': 4.5,
    'starpilot': 2.5,
}

rMax = {
    'bigfish': 40,
    'bossfight': 13,
    'caveflyer': 12,
    'chaser': 13,
    'climber': 12.6,
    'coinrun': 10,
    'dodgeball': 19,
    'fruitbot': 32.4,
    'heist': 10,
    'jumper': 10,
    'leaper': 10,
    'maze': 10,
    'miner': 13,
    'ninja': 10,
    'plunder': 30,
    'starpilot': 64,
}

environments = ['bigfish', 'bossfight', 'caveflyer', 'chaser', 'climber', 'coinrun', 'dodgeball', 'fruitbot', 'heist', 'jumper', 'leaper', 'maze', 'miner', 'ninja', 'plunder', 'starpilot']
# environments = ['chaser']
environments = ['bigfish']
for env in environments:
    evaluate(f'Final_stateUncertainty0.25and0bigfish', env)

# V1
# n=20000
# Base_bigfish-0        0.15    7.07592190889371
# Base_bossfight-0     -0.02    0.21374045801526717
# Base_caveflyer-0     -0.35    0.4662004662004662
# Base_chaser-0        -0.01    0.29332746983281394
# Base_climber-0       -0.18    0.0
# Base_coinrun-0       -0.22    3.876923076923077
# Base_dodgeball-0     -0.03    0.9487516425755584
# Base_fruitbot-0       0.7     22.550248756218906
# Base_heist-0         -0.5     0.24937655860349128
# Base_jumper-0         0.37    5.598214285714286
# Base_leaper-0         0.14    3.990216631726066
# Base_maze-0          -0.69    1.5217391304347827
# Base_miner-0         -0.12    0.1025
# Base_ninja-0         -0.53    0.0
# Base_plunder-0       -0.1     1.7273579013116802
# Base_starpilot-0      0.15    12.261037955073586

# V2
# n=20000
# Base_v2_bigfish-0    0.0    0.9819785276073619
# Base_v2_fruitbot-0   0.79    25.30938123752495
# Base_v2_jumper-0     0.78    8.515264660663298
# Base_v2_leaper-0     0.56    6.9545071609098565
# Base_v2_chaser-0     0.0    0.48920573588025446
# Base_v2_bossfight-0  0.65    8.725255972696246
# Base_v2_starpilot-0  0.49    32.96410767696909
