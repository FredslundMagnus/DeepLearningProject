from collector import Collector
from environments import Environments
from Utils.server import isServer, params, serverRun, saveAgent, saveCollector
from agent import Agent
from display_input import displayer
from Utils.debug import disablePrint
from time import time
from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU
from helpers import hidden_size
from display_input import showFilters, returnplot
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


# class NetWork(Module):
#     def __init__(self):
#         self.size_after_conv = 128

#         super(NetWork, self).__init__()

#         self.color = Sequential(
#             Conv2d(in_channels=3, out_channels=8, kernel_size=1, stride=1),
#             LeakyReLU(),
#             Conv2d(in_channels=8, out_channels=16, kernel_size=4, stride=2),
#             LeakyReLU(),
#         )

#         self.conv1 = Sequential(
#             Conv2d(in_channels=16, out_channels=32, kernel_size=4, stride=1),
#             MaxPool2d(2, 2, padding=0),
#             LeakyReLU(),
#             Conv2d(in_channels=32, out_channels=64, kernel_size=4, stride=2),
#             LeakyReLU(),
#             Conv2d(in_channels=64, out_channels=64, kernel_size=4, stride=1),
#             LeakyReLU(),
#             Conv2d(in_channels=64, out_channels=self.size_after_conv, kernel_size=3, stride=1),
#             LeakyReLU(),
#         )

#         self.fromEncoder = Sequential(
#             Conv2d(in_channels=12, out_channels=32, kernel_size=4, stride=2),
#             LeakyReLU(),
#             Conv2d(in_channels=32, out_channels=self.size_after_conv, kernel_size=4, stride=1),
#             LeakyReLU(),
#         )

#         self.lstm = LSTM(self.size_after_conv, hidden_size, 1)

#         self.linear = Sequential(
#             LeakyReLU(),
#             Linear(hidden_size, 15),
#         )

#         self.exploration_network = Sequential(
#             LeakyReLU(),
#             Linear(hidden_size, hidden_size),
#             LeakyReLU(),
#             Linear(hidden_size, 15),
#         )

#  def forward(self, x):
#       self.lstm.flatten_parameters()
#        if self.hasEncoder:
#             x = self.fromEncoder(x)
#         else:
#             x = self.color(x)
#             x = self.conv1(x)
#         x = x.view(1, -1, self.size_after_conv)
#         x, (self.hn, self.cn) = self.lstm(x, (self.hn, self.cn))
#         x = x.view(-1, hidden_size)
#         y = x.clone()
#         y = self.exploration_network(y.detach())
#         x = self.linear(x)
#         return x, y


if isServer:
    # the server runs the main function (can be changed)
    def main():
        name, environment, hours, total_agents = params['name'], params['environment'], params['hours'], params['total_agents']
        agent = Agent(**params)
        env = Environments(render=False, envs=[environment for _ in range(total_agents)], agent=agent)
        collector = Collector(**params)
        tid = time() + 3600 * hours - 300
        while time() < tid:
            obs, hn, cn = env.start()
            act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
            obs, rew, done, info = env.step(act, hn, cn)
            collector.collect(rew, done, act)
            agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)
            agent.learn()
        saveAgent(agent, name)
        saveCollector(collector, name)
    serverRun()
else:
    total_agents, display_every = 20, 5000
    agent = Agent(memory=40000, discount=0.995, update_every=100, double=True, uncertainty=True, state_difference=True, uncertainty_weight=0, state_difference_weight=0)
    env = Environments(render=True, envs=['maze' for _ in range(total_agents)], agent=agent)
    collector = Collector(calculate_every=500, total_agents=total_agents)
    for f in range(1, 10000000):
        obs, hn, cn = env.start()
        act, obs_old, h0, c0, hn, cn = agent.chooseMulti(obs, hn, cn)
        obs, rew, done, info = env.step(act, hn, cn)
        collector.collect(rew, done, act)
        agent.rememberMulti(obs_old, act, obs, rew, h0, c0, hn, cn, done)
        agent.learn()

        if showPrint:
            plt.close('all')
            showFilters(obs[0], y=200, x=600)
            returnplot(collector.all_return, x=1200, y=200)
            showPrint = False
