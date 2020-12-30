import pickle
from environments import Environments
from display_input import displayer
import matplotlib.pyplot as plt


def showcase(name, environment, n=0, max_values=True, done=None):
    name = name + '-' + str(n)
    agent = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.agent", "rb"))
    # agent.exploration.counter = 10000000
    if max_values == True:
        agent.explore = agent.exploration.greedy
        agent.uncertainty_weight = -0
        agent.state_avoidance = False
    env = Environments(render=True, envs=[environment], agent=agent)
    collector = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Collectors/{name}.collect", "rb"))
    for i in range(10000):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn, before_trace, after_trace = agent.chooseMulti(obs, hn, cn, done=done)
        obs, rew, done, info = env.step(act, hn, cn)

        if i == 10:
            displayer(obs[0].cpu(), agent, collector, environment=environment)


# Base_bigfish-0 5.264150943396227
# Base_bossfight-0 0.0
# Base_caveflyer-0 0.575
# Base_chaser-0 0.30036529008996543
# Base_climber-0 0.0
# Base_coinrun-0 4.2592592592592595
# Base_dodgeball-0 0.8201438848920863
# Base_fruitbot-0 22.11111111111111
# Base_heist-0 0.7317073170731707
# Base_jumper-0 6.25

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

env = 'chaser'
showcase(f'NOPE_final_{env}', env, max_values=True)


['bigfish', 'bossfight', 'caveflyer', 'chaser', 'climber', 'coinrun', 'dodgeball', 'fruitbot', 'heist', 'jumper', 'leaper', 'maze', 'miner', 'ninja', 'plunder', 'starpilot']
