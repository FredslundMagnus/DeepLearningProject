from collector import Collector
from environments import Environments
from Utils.server import isServer, params, serverRun, saveAgent, saveCollector
from agent import Agent
from display_input import displayer
from Utils.debug import disablePrint
from time import time
from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU
from helpers import hidden_size
from display_input import showFilters, returnplot, displayer
import matplotlib.pyplot as plt

showPrint, save = False, False

if not isServer:
    from pynput import keyboard

    def on_press(key):
        global showPrint, save
        if keyboard.Key.f2 == key:
            showPrint = True
        if keyboard.Key.f3 == key:
            save = True

    keyboard.Listener(on_press=on_press).start()


class NetWork(Module):
    def __init__(self, h):
        self.size_after_conv = 128
        self.hidden_size = h
        self.current_state = None

        super(NetWork, self).__init__()

        self.color = Sequential(
            Conv2d(in_channels=3, out_channels=8, kernel_size=1, stride=1),
            LeakyReLU(),
            Conv2d(in_channels=8, out_channels=16, kernel_size=4, stride=2),
            LeakyReLU(),
        )

        self.conv1 = Sequential(
            Conv2d(in_channels=16, out_channels=32, kernel_size=4, stride=1),
            MaxPool2d(2, 2, padding=0),
            LeakyReLU(),
            Conv2d(in_channels=32, out_channels=64, kernel_size=4, stride=2),
            LeakyReLU(),
            Conv2d(in_channels=64, out_channels=64, kernel_size=4, stride=1),
            LeakyReLU(),
            Conv2d(in_channels=64, out_channels=self.size_after_conv, kernel_size=3, stride=1),
            LeakyReLU(),
        )

        self.fromEncoder = Sequential(
            Conv2d(in_channels=12, out_channels=32, kernel_size=4, stride=1),
            LeakyReLU(),
            Conv2d(in_channels=32, out_channels=64, kernel_size=4, stride=1),
            LeakyReLU(),
            Conv2d(in_channels=64, out_channels=self.size_after_conv, kernel_size=4, stride=1),
            LeakyReLU(),
        )

        self.lstm = LSTM(self.size_after_conv, self.hidden_size, 1)

        self.linear = Sequential(
            LeakyReLU(),
            Linear(self.hidden_size, 15),
        )

        self.exploration_network = Sequential(
            LeakyReLU(),
            Linear(self.hidden_size, self.hidden_size),
            LeakyReLU(),
            Linear(self.hidden_size, self.hidden_size // 2),
            LeakyReLU(),
            Linear(self.hidden_size // 2, 15),
        )

        self.state_difference_network = Sequential(
            Linear(self.size_after_conv, self.size_after_conv),
            LeakyReLU(),
            Linear(self.size_after_conv, self.hidden_size),
            LeakyReLU(),
            Linear(self.hidden_size, 15),
        )


if isServer:
    # the server runs the main function (can be changed)
    def main():
        name, environment, hours, total_agents, done = params['name'], params['environment'], params['hours'], params['total_agents'], None
        agent = Agent(**params)
        env = Environments(render=False, envs=[environment for _ in range(total_agents)], agent=agent)
        collector = Collector(**params)
        tid, f = time() + 3600 * hours - 300, 0
        while time() < tid:
            f += 1
            obs, hn, cn = env.start()
            act, obs_old, h0, c0, hn, cn, before_trace, after_trace = agent.chooseMulti(obs, hn, cn, done=done)
            obs, rew, done, info = env.step(act, hn, cn)
            collector.collect(rew, done, act, agent.onpolicy)
            if not agent.onpolicy and f > 10:
                agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done, before_trace, after_trace)
            agent.learn()
        saveAgent(agent, name)
        saveCollector(collector, name)
    serverRun()
else:
    total_agents, display_every, done = 20, 5000, None
    agent = Agent(memory=40000, discount=0.99, uncertainty=1, state_difference=1, uncertainty_weight=0.1, state_difference_weight=0.1, exploration='epsintosoftmax')
    env = Environments(render=True, envs=['maze' for _ in range(total_agents)], agent=agent)
    collector = Collector(calculate_every=500, total_agents=total_agents)
    for f in range(1, 10000000):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn, before_trace, after_trace = agent.chooseMulti(obs, hn, cn, done=done)
        obs, rew, done, info = env.step(act, hn, cn)
        collector.collect(rew, done, act, agent.onpolicy)
        if not agent.onpolicy and f > 10:
            agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done, before_trace, after_trace)
        agent.learn()

        if showPrint:
            plt.close('all')
            #showFilters(obs[0], y=200, x=600)
            #returnplot(collector.all_return, x=1200, y=200)
            displayer(obs[0], agent, collector)
            showPrint = False
