import pickle
from environments import Environments
from display_input import displayer
import matplotlib.pyplot as plt


def showcase(name, environment, n=0, max_values=True, done=None):
    name = name + '-' + str(n)
    agent = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.agent", "rb"))
    if max_values == True:
        agent.explore = agent.exploration.greedy
        agent.uncertainty = False
        agent.state_avoidance = False
    env = Environments(render=True, envs=[environment], agent=agent)
    collector = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Collectors/{name}.collect", "rb"))
    for i in range(10000):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn, before_trace, after_trace = agent.chooseMulti(obs, hn, cn, done=done)
        obs, rew, done, info = env.step(act, hn, cn)

        if i == 100:
            displayer(obs[0].cpu(), agent, collector)


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

env = 'maze'
showcase('MAZE_U_S_0.1_0returnmaze', env, max_values=False)
