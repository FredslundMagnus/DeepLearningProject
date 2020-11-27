from collector import Collector
from environments import Environments
from Utils.server import isServer, params, serverRun, saveAgent, saveCollector
from agent import Agent
from display_input import displayer
from Utils.debug import disablePrint
from time import time
from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU
from pynput import keyboard
from display_input import showFilters, returnplot
import matplotlib.pyplot as plt
showPrint, save = False, False


def on_press(key):
    global showPrint, save
    if keyboard.Key.f2 == key:
        showPrint = True
    if keyboard.Key.f3 == key:
        save = True


keyboard.Listener(on_press=on_press).start()


total_agents, display_every = 20, 5000
agent = Agent(memory=40000, discount=0.995, uncertainty=False, update_every=100, double=True, use_distribution=False, reward_normalization=False)
env = Environments(render=True, envs=['fruitbot' for _ in range(total_agents)], agent=agent)
collector = Collector(calculate_every=500, total_agents=total_agents)
for f in range(10000000):
    obs, hn, cn = env.start()
    act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
    obs, rew, done, info = env.step(act, hn, cn)
    collector.collect(rew, done, act)
    agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)
    agent.learn()

    if showPrint:
        plt.close('all')
        displayer(obs[0].cpu(), agent, collector)
        plt.plot(h0[0].cpu().numpy().reshape(-1))
        showPrint = False
