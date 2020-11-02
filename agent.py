"""
[1] https://www.element61.be/en/resource/quick-guide-reinforcement-learning-and-how-experiment-using-openai-gym
"""


from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential
from torch.optim import Adam
from memory import ReplayBuffer
from exploration import Exploration
import torch
from helpers import device, hidden_size, count_parameters
import copy


class Agent:
    def __init__(self) -> None:
        self.network = NetWork()
        self.network.to(device).cuda()
        print("Number of parameters in network:", count_parameters(self.network))
        self.criterion = MSELoss()
        self.optimizer = Adam(self.network.parameters(), lr=1e-3, weight_decay=1e-5)
        self.memory = ReplayBuffer(10000)
        self.remember = self.memory.remember()
        self.exploration = Exploration()
        self.explore = self.exploration.softmax
        self.target_network = copy.deepcopy(self.network)

    def choose(self, pixels, hn, cn):
        self.network.hn, self.network.cn = hn, cn
        vals = self.network(pixels).reshape(15)
        return self.explore(vals), pixels, hn, cn, self.network.hn, self.network.cn

    def learn(self, double=False):
        gamma = 0.98
        obs, action, obs_next, reward, h0, c0, hn, sn, done = self.memory.sample(20)
        self.network.hn, self.network.cn = hn, sn

        if double:
            v_s_next = torch.gather(self.target_network(obs_next), 1, torch.argmax(self.network(obs_next), 1).view(-1, 1)).squeeze(1)
        else:
            v_s_next, input_indexes = torch.max(self.target_network(obs_next), 1)

        self.network.hn, self.network.cn = h0, c0
        v_s = torch.gather(self.network(obs), 1, action)
        #v_s, _ = torch.max(self.network(obs), 1)
        td = (reward + gamma * v_s_next * done.type(torch.float)).detach().view(-1, 1)
        loss = self.criterion(v_s, td)
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
        torch.cuda.empty_cache()

    def update_target_network(self):
        self.target_network = copy.deepcopy(self.network)


class NetWork(Module):
    def __init__(self):
        super(NetWork, self).__init__()

        self.conv1 = Sequential(
            Conv2d(in_channels=3, out_channels=8, kernel_size=1),
            Conv2d(in_channels=8, out_channels=16, kernel_size=8, stride=4),
            LeakyReLU(),
            Conv2d(in_channels=16, out_channels=32, kernel_size=4, stride=2),
            LeakyReLU(),
            Conv2d(in_channels=32, out_channels=32, kernel_size=3),
            LeakyReLU(),
        )

        # self.conv2 = Sequential(
        #     Conv2d(in_channels=15, out_channels=20, kernel_size=3),
        #     LeakyReLU(),
        #     Conv2d(in_channels=20, out_channels=25, kernel_size=3),
        #     MaxPool2d(2, 2, padding=0),
        #     LeakyReLU(),
        # )

        # self.conv3 = Sequential(
        #     Conv2d(in_channels=25, out_channels=20, kernel_size=1),
        #     LeakyReLU(),
        #     Conv2d(in_channels=20, out_channels=15, kernel_size=3),
        #     # MaxPool2d(2, 2, padding=0),
        #     LeakyReLU(),
        # )

        # self.size_after_conv = 720
        # self.lstm = LSTM(self.size_after_conv, hidden_size, 2)

        self.linear = Sequential(
            Linear(512, 100),
            # Linear(hidden_size, 40),
            LeakyReLU(),
            Linear(100, 15),
        )

    def forward(self, x):
        x = self.conv1(x)
        #x = self.conv2(x)
        #x = self.conv3(x)

        # x = x.view(1, -1, self.size_after_conv)
        # x, (self.hn, self.cn) = self.lstm(x, (self.hn, self.cn))
        # x = x.view(-1, hidden_size)
        x = x.view(-1, 512)
        x = self.linear(x)
        return x


if __name__ == "__main__":
    from torch import rand
    from time import time
    from helpers import stack
    a = rand((1, 3, 64, 64))
    agent = Agent()
    for _ in range(1000):
        agent.remember(a, 23, a, 0.0)

    sample = agent.memory.sample(20)
    start = time()
    for i in range(10000):
        stack(sample)
    end = time()
    print(end - start)
    sample = agent.memory.sample(25)
    start = time()
    for i in range(10000):
        stack(sample)
    end = time()
    print(end - start)
