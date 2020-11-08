import pickle
from environments import Environments
from display_input import displayer


def showcase(name, environment):
    agent = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.agent", "rb"))
    env = Environments(render=True, envs=[environment])
    all_return = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Means/{name}.means", "rb"))
    for i in range(10000):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
        obs, rew, done, info = env.step(act, hn, cn)

        if i % 1000 == 0:
            displayer(obs[0].cpu(), agent, all_return, [1, 1])


showcase('Discount_0.9_1-0', 'fruitbot')
