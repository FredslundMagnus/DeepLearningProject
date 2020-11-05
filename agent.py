"""
[1] https://www.element61.be/en/resource/quick-guide-reinforcement-learning-and-how-experiment-using-openai-gym
"""


from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU
from torch.optim import Adam
from memory import ReplayBuffer
from exploration import Exploration
import torch
from helpers import device, hidden_size, count_parameters
import copy


class Agent:
    def __init__(self, memory=50000, gamma=0.99) -> None:
        self.network = NetWork().to(device)
        print("Number of parameters in network:", count_parameters(self.network))
        self.criterion = MSELoss()
        self.optimizer = Adam(self.network.parameters(), lr=1e-4, weight_decay=1e-5)
        self.memory = ReplayBuffer(memory)
        self.remember = self.memory.remember()
        self.exploration = Exploration()
        self.explore = self.exploration.softmax
        self.target_network = NetWork().to(device)
        self.placeholder_network = NetWork().to(device)
        self.gamma = gamma

    def choose(self, pixels, hn, cn):
        self.network.hn, self.network.cn = hn, cn
        vals = self.network(pixels).reshape(15)
        return self.explore(vals), pixels, hn, cn, self.network.hn, self.network.cn

    def learn(self, double=False):
        obs, action, obs_next, reward, h0, c0, hn, sn, done = self.memory.sample_distribution(20)
        self.network.hn, self.network.cn = hn, sn
        if double:
            v_s_next = torch.gather(self.target_network(obs_next), 1, torch.argmax(self.network(obs_next), 1).view(-1, 1)).squeeze(1)
        else:
            v_s_next, input_indexes = torch.max(self.target_network(obs_next), 1)

        self.network.hn, self.network.cn = h0, c0
        v_s = torch.gather(self.network(obs), 1, action)
        #v_s, _ = torch.max(self.network(obs), 1)
        td = (reward + self.gamma * v_s_next * done.type(torch.float)).detach().view(-1, 1)
        loss = self.criterion(v_s, td)

        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
        torch.cuda.empty_cache()

    def update_target_network(self):
        self.target_network = copy.deepcopy(self.placeholder_network)
        self.placeholder_network = copy.deepcopy(self.network)
        self.memory.update_distribution()


class NetWork(Module):
    def __init__(self):
        super(NetWork, self).__init__()

        self.color = Sequential(MaxPool2d(2, 2, padding=0))

        self.conv1 = Sequential(
            Conv2d(in_channels=3, out_channels=10, kernel_size=4, stride=2),
            LeakyReLU(),
            Conv2d(in_channels=10, out_channels=16, kernel_size=4, stride=1),
            MaxPool2d(2, 2, padding=0),
            LeakyReLU(),
            Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1),
            LeakyReLU(),
            Conv2d(in_channels=32, out_channels=32, kernel_size=2, stride=1),
            LeakyReLU(),
        )
        self.linear = Sequential(
            Linear(288, 64),
            LeakyReLU(),
            Linear(64, 15),
        )

    def forward(self, x):
        x = self.color(x)
        x = self.conv1(x)
        x = x.view(-1, 288)
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
