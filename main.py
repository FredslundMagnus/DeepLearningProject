from environments import Environment
from Utils.server import isServer, params, serverRun
from agent import Agent
from helpers import clean, hidden_size, device
import torch
# import glfw


if isServer:
    name, lossf, discount, lambd, lr, dropout = params
    print(name, lossf, discount, lambd, lr, dropout)

    # the server runs the main function (can be changed)
    def main():
        env = Environment(render=False).coinrun  # env = Environment(render=True)["coinrun"]
        agent = Agent()
        for i in range(1):
            obs = clean(env.reset())
            while True:
                act, obs_old = agent.choose(obs)  # env.action_space.sample()
                obs, rew, done, info = env.step(act)
                obs = agent.remember(obs_old, act, clean(obs), rew)
                agent.learn()
                env.render()
                if done:
                    break
    serverRun()
else:
    agent = Agent()
    env = Environment(render=True).bigfish  # env = Environment(render=True)["coinrun"]
    for i in range(10000):
        obs = clean(env.reset())
        hn = torch.zeros(2, 1, hidden_size).to(device)
        cn = torch.zeros(2, 1, hidden_size).to(device)
        total_rew = 0
        print(torch.cuda.memory_allocated())
        while True:

            act, obs_old, h0, c0, hn, cn = agent.choose(obs, hn, cn)  # env.action_space.sample()
            obs, rew, done, info = env.step(act)
            obs = agent.remember(obs_old, act, clean(obs), rew, h0, c0, hn, cn, int(not done))
            agent.learn()
            # glfw.terminate()
            env.render()
            total_rew += rew
            if done:
                print(f"\n{i}. Total reward: {total_rew}")
                break
        env.close()
