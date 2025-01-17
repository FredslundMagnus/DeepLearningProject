import pickle
from environments import Environments
from Utils.debug import disablePrint, enablePrint


def evaluate(name, environment, n=0, uncertainty=0):
    disablePrint()
    name = name + '-' + str(n)
    agent = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.agent", "rb"))
    agent.explore = agent.exploration.greedy
    agent.uncertainty = True
    agent.state_avoidance = False
    agent.uncertainty_weight = uncertainty
    env = Environments(render=False, envs=[environment for _ in range(20)], agent=agent)
    rews, dones = [], []
    for i in range(20000):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn, _, _ = agent.chooseMulti(obs, hn, cn)
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
for env in environments:
    evaluate(f'NOPE_final_{env}', env)


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
# Base_v2_bigfish-0    0.0    0.9227373068432672
# Base_v2_bossfight-0  0.68    9.01056338028169
# Base_v2_caveflyer-0  0.02    3.6844444444444444
# Base_v2_chaser-0     0.0    0.505568357727673
# Base_v2_climber-0    0.0    2.0677290836653386
# Base_v2_coinrun-0    -0.31    3.443708609271523
# Base_v2_dodgeball-0  0.15    4.24537037037037
# Base_v2_fruitbot-0   0.8    25.635627530364374
# Base_v2_heist-0      -0.49    0.29850746268656714
# Base_v2_jumper-0     0.8    8.617814831066257
# Base_v2_leaper-0     0.56    6.9608659450457955
# Base_v2_maze-0       -0.46    2.6923076923076925
# Base_v2_miner-0      -0.11    0.16831683168316833
# Base_v2_ninja-0      -0.08    2.943396226415094
# Base_v2_plunder-0    0.15    8.524390243902438
# Base_v2_starpilot-0  0.47    31.75

# NOPE
# n=20000
# NOPE_final_bigfish-0 0.19    8.65365025466893
# NOPE_final_bossfight-0 0.52    7.021459227467811
# NOPE_final_caveflyer-0 0.05    3.9856972586412396
# NOPE_final_chaser-0  0.08    1.58410132545602
# NOPE_final_climber-0 0.0    2.0
# NOPE_final_coinrun-0 -0.18    4.065155807365439
# NOPE_final_dodgeball-0 -0.05    0.5059493016037248
# NOPE_final_fruitbot-0 0.75    24.081967213114755
# NOPE_final_heist-0   -0.47    0.4444444444444444
# NOPE_final_jumper-0  0.62    7.400084139671855
# NOPE_final_leaper-0  0.07    3.556019485038274
# NOPE_final_maze-0    -0.2    3.998294970161978
# NOPE_final_miner-0   0.0    1.459090909090909
# NOPE_final_ninja-0   -0.06    3.083219645293315
# NOPE_final_plunder-0 -0.04    3.3014586709886546
# NOPE_final_starpilot-0 0.58    38.21848739495798