from environments import Environment
from Utils.server import isServer, params, printInfo
from agent import Agent
from helpers import clean


if isServer:
    name, lossf, discount, lambd, lr, dropout = params
    print(name, lossf, discount, lambd, lr, dropout)

    # the server runs the main function (can be changed)
    def main():
        env = Environment(render=False).coinrun  # env = Environment(render=True)["coinrun"]
        agent = Agent()
        for i in range(10):
            obs = clean(env.reset())
            while True:
                act, obs_old = agent.choose(obs)  # env.action_space.sample()
                obs, rew, done, info = env.step(act)
                obs = agent.remember(obs_old, act, clean(obs), rew)
                agent.learn()
                env.render()
                if done:
                    break
    printInfo()
else:
    env = Environment(render=True).coinrun  # env = Environment(render=True)["coinrun"]
    agent = Agent()
    obs = clean(env.reset())
    while True:
        act, obs_old = agent.choose(obs)  # env.action_space.sample()
        obs, rew, done, info = env.step(act)
        obs = agent.remember(obs_old, act, clean(obs), rew)
        agent.learn()
        env.render()
        if done:
            break
    env.close()
    print(agent.memory.sample(5))
