from environments import Environment
from Utils.server import isServer, params
from agent import Agent


if isServer:
    name, lossf, discount, lambd, lr, dropout = params
    print(name, lossf, discount, lambd, lr, dropout)
else:
    env = Environment(render=True).coinrun  # env = Environment(render=True)["coinrun"]
    agent = Agent()
    obs = env.reset()
    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        if done:
            break
    env.close()
