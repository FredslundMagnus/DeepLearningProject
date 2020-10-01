from environments import Environment
from Utils.server import isServer, params
from agent import Agent


if isServer:
    name, lossf, discount, lambd, lr, dropout = params
    print(name, lossf, discount, lambd, lr, dropout)
else:
    env = Environment(render=True).coinrun  # env = Environment(render=True)["coinrun"]
    agent = Agent()
    obs_old = env.reset()
    while True:
        act = env.action_space.sample()
        obs, rew, done, info = env.step(act)
        agent.remember(obs, act, obs_old, rew)
        env.render()
        if done:
            break
        obs_old = obs
    env.close()
    print(agent.memory.sample(5))
