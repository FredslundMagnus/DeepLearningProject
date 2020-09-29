import gym
from Utils.server import isServer, params


if isServer:
    name, lossf, discount, lambd, lr, dropout = params
    print(name, lossf, discount, lambd, lr, dropout)
else:
    env = gym.make("procgen:procgen-coinrun-v0", render_mode="human")
    obs = env.reset()
    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        if done:
            break
    env.close()
