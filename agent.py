"""
[1] https://www.element61.be/en/resource/quick-guide-reinforcement-learning-and-how-experiment-using-openai-gym
"""


from torch import squeeze
from torch.nn import Module, Conv2d, MaxPool2d, Linear, CrossEntropyLoss
from torch.nn.functional import relu
from torch.optim import Adam
from memory import ReplayBuffer
from exploration import Exploration
import torch


class Agent:
    def __init__(self) -> None:
        self.network = NetWork()
        self.criterion = CrossEntropyLoss()
        self.optimizer = Adam(self.network.parameters(), lr=3e-4, weight_decay=1e-5)
        self.memory = ReplayBuffer(1000)
        self.remember = self.memory.remember()
        self.exploration = Exploration()
        self.explore = self.exploration.softmax

    def choose(self, pixels):
        vals = self.network(pixels).reshape(15)
        return self.explore(vals), pixels

    def learn(self):
        gamma = 0.99
        obs, action, obs_next, reward = self.memory.sample(2)
        v_s_next, input_indexes = torch.max(self.network(obs_next), 1)
        v_s = torch.gather(self.network(obs), 1, action).squeeze(1)
        td = reward + gamma * v_s_next - v_s


class NetWork(Module):
    def __init__(self):
        super(NetWork, self).__init__()

        self.conv1 = Conv2d(in_channels=3, out_channels=10, kernel_size=3)
        self.pool = MaxPool2d(2, 2)
        self.conv2 = Conv2d(in_channels=10, out_channels=20, kernel_size=3)
        self.size_after_conv = 3920
        self.fc1 = Linear(self.size_after_conv, 120)
        self.fc2 = Linear(120, 60)
        self.fc3 = Linear(60, 15)

    def forward(self, x):
        x = self.pool(relu(self.conv1(x)))
        x = self.pool(relu(self.conv2(x)))
        x = x.view(-1, self.size_after_conv)
        x = relu(self.fc1(x))
        x = relu(self.fc2(x))
        x = self.fc3(x)
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
