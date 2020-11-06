from environments import Environment, Environments
from agent import Agent
from helpers import clean, hidden_size, device
import torch
import time
from Utils.debug import disablePrint, enablePrint
from display_input import displayer
from runningList import RunningList
import matplotlib.pyplot as plt

# agent = Agent()
# env = Environment(render=False).fruitbot
# # env = Environment(render=False)["coinrun"]
# # envs = Environments(['bigfish'], render=True)
# n = 20000
# k = 5
# disablePrint()
# t0 = time.time()
# for i in range(n):
#     obs, rev, done, info = env.step(1)
#     env.render()
#     if done:
#         env.close()
#         env.reset()
# t1 = time.time()
# enablePrint()
# print("Step", t1 - t0)  # 1

# env.close()
# obs = clean(env.reset())
# hn = torch.zeros(1, 1, hidden_size, device=device)
# cn = torch.zeros(1, 1, hidden_size, device=device)
# disablePrint()
# t0 = time.time()
# for i in range(n):
#     agent.choose(obs, hn, cn)
# t1 = time.time()
# enablePrint()
# print("Choose", t1 - t0)  # 48

# env.close()
# obs = clean(env.reset())
# hn = torch.zeros(1, 1, hidden_size, device=device)
# cn = torch.zeros(1, 1, hidden_size, device=device)
# disablePrint()
# t0 = time.time()
# obs, hn, cn = [obs for _ in range(k)], [hn for _ in range(k)], [cn for _ in range(k)]
# for i in range(n // k):
#     agent.chooseMulti(obs, hn, cn)
# t1 = time.time()
# enablePrint()
# print("Choose", t1 - t0)  # 17.568519115447998


agent = Agent()
env = Environments(render=True, envs=['chaser' for _ in range(20)])
li = RunningList(500)
mean = []
all_return = []
update_every = 100
disablePrint()
frames = 1000000
dones, total_rew = 0, 0
for f in range(1, frames + 1):
    obs, hn, cn = env.start()
    act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
    obs, rew, done, info = env.step(act, hn, cn)
    total_rew += sum(rew) / len(rew)
    dones += sum(done) / len(done)
    agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)
    if f > update_every:
        for _ in range(3):
            agent.learn(double=True)
    if f % update_every == 0:
        agent.update_target_network()
        all_return.append(total_rew / dones)
        dones, total_rew = 0, 0
    if f % (10 * update_every) == 0:
        displayer(obs[0].cpu(), agent, all_return)
