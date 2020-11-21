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
    evaluate(f'Base_{env}', env)



# Base_bigfish-0 8.064516129032258
# Base_bossfight-0 0.25
# Base_caveflyer-0 1.0
# Base_chaser-0 0.32498905181689125
# Base_climber-0 0.0
# Base_coinrun-0 4.2592592592592595
# Base_dodgeball-0 0.9873417721518988
# Base_fruitbot-0 22.793478260869566
# Base_heist-0 0.4878048780487805
# Base_jumper-0 6.666666666666667
# Base_leaper-0 4.661654135338346
# Base_maze-0 1.1111111111111112
# Base_miner-0 0.15
# Base_ninja-0 0.0
# Base_plunder-0 1.8038585209003215