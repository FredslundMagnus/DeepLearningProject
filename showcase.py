import pickle
from environments import Environments
from display_input import displayer


def showcase(name, environment, n=0):
    name = name + '-' + str(n)
    agent = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.agent", "rb"))
    agent.explore = agent.exploration.greedy
    env = Environments(render=True, envs=[environment])
    collector = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Collectors/{name}.collect", "rb"))
    for i in range(10000):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
        obs, rew, done, info = env.step(act, hn, cn)

        if i == 30:
            displayer(obs[0].cpu(), agent, collector)


showcase('Dist_eps', 'fruitbot')
