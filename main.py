import gym
import sys
from Utils.server import getvals
params = sys.argv[1:]
if params:
    name, lossf, discount, lambd, lr, dropout = getvals(params)
    print(name, lossf, discount, lambd, lr, dropout)
else:
    env = gym.make('procgen:procgen-coinrun-v0')
    obs = env.reset()
    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        if done:
            break
