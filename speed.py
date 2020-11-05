from environments import Environment
from agent import Agent
from helpers import clean, hidden_size, device
import torch
import time
from Utils.debug import disablePrint, enablePrint


agent = Agent()
env = Environment(render=False).fruitbot  # env = Environment(render=True)["coinrun"]
n = 20000
k = 20
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

env.close()
obs = clean(env.reset())
hn = torch.zeros(2, 1, hidden_size, device=device)
cn = torch.zeros(2, 1, hidden_size, device=device)
disablePrint()
t0 = time.time()
obs, hn, cn = [obs for _ in range(k)], [hn for _ in range(k)], [cn for _ in range(k)]
for i in range(n // k):
    act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
t1 = time.time()
enablePrint()
print("Choose", t1 - t0)  # 40
