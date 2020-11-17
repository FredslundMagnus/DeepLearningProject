import pickle
from environments import Environments
from Utils.debug import disablePrint, enablePrint


def evaluate(name, environment, n=0):
    disablePrint()
    name = name + '-' + str(n)
    agent = pickle.load(open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.agent", "rb"))
    agent.explore = agent.exploration.greedy
    env = Environments(render=False, envs=[environment for _ in range(20)])
    rews, dones = [], []
    for i in range(2000):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
        obs, rew, done, info = env.step(act, hn, cn)
        rews.append(sum(rew))
        dones.append(sum(done))
    enablePrint()
    print(name, sum(rews) / sum(dones))


evaluate('Dist', 'fruitbot')
evaluate('Dist_eps', 'fruitbot')
