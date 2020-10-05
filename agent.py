"""
[1] https://www.element61.be/en/resource/quick-guide-reinforcement-learning-and-how-experiment-using-openai-gym
"""


from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM
from torch.nn.functional import leaky_relu
from torch.optim import Adam
from torch.optim import optimizer
from memory import ReplayBuffer
from exploration import Exploration
import torch
from helpers import device, hidden_size


class Agent:
    def __init__(self) -> None:
        self.network = NetWork()
        self.network.to(device)
        self.criterion = MSELoss()
        self.optimizer = Adam(self.network.parameters(), lr=3e-4, weight_decay=1e-5)
        self.memory = ReplayBuffer(1000)
        self.remember = self.memory.remember()
        self.exploration = Exploration()
        self.explore = self.exploration.softmax

    def choose(self, pixels, hn, cn):
        self.network.hn, self.network.cn = hn, cn
        vals = self.network(pixels).reshape(15)
        return self.explore(vals), pixels, hn, cn, self.network.hn, self.network.cn

    def learn(self):
        gamma = 0.99
        obs, action, obs_next, reward, h0, c0, hn, sn, done = self.memory.sample(20)
        self.network.hn, self.network.cn = hn, sn
        v_s_next, input_indexes = torch.max(self.network(obs_next), 1)
        self.network.hn, self.network.cn = h0, c0
        v_s = torch.gather(self.network(obs), 1, action).squeeze(1)
        td = (reward + gamma * v_s_next * done).detach()
        loss = self.criterion(v_s, td)
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
        torch.cuda.empty_cache()


class NetWork(Module):
    def __init__(self):
        super(NetWork, self).__init__()

        self.conv1_1_1 = Conv2d(in_channels=3, out_channels=10, kernel_size=1)
        self.conv1_3_1 = Conv2d(in_channels=10, out_channels=10, kernel_size=3)
        self.conv1_1_2 = Conv2d(in_channels=10, out_channels=20, kernel_size=1)
        self.conv1_3_2 = Conv2d(in_channels=20, out_channels=20, kernel_size=3)
        self.pool1 = MaxPool2d(2, 2, padding=0)
        self.conv2_1 = Conv2d(in_channels=20, out_channels=30, kernel_size=1)
        self.conv2_3 = Conv2d(in_channels=30, out_channels=30, kernel_size=3)
        self.pool2 = MaxPool2d(2, 2, padding=0)
        self.conv3_1 = Conv2d(in_channels=30, out_channels=40, kernel_size=1)
        self.conv3_3 = Conv2d(in_channels=40, out_channels=40, kernel_size=3)
        self.pool3 = MaxPool2d(2, 2, padding=0)
        self.size_after_conv = 1440
        self.lstm = LSTM(self.size_after_conv, hidden_size, 2)
        self.fc1 = Linear(hidden_size, 120)
        self.fc2 = Linear(120, 60)
        self.fc3 = Linear(60, 15)

    def forward(self, x):
        x = leaky_relu(self.conv1_1_1(x))
        x = leaky_relu(self.conv1_3_1(x))
        x = leaky_relu(self.conv1_1_2(x))
        x = self.pool1(leaky_relu(self.conv1_3_2(x)))
        x = leaky_relu(self.conv2_1(x))
        x = self.pool2(leaky_relu(self.conv2_3(x)))
        x = leaky_relu(self.conv3_1(x))
        x = self.pool3(leaky_relu(self.conv3_3(x)))
        x = x.view(1, -1, self.size_after_conv)
        x, (self.hn, self.cn) = self.lstm(x, (self.hn, self.cn))
        x = x.view(-1, hidden_size)
        x = leaky_relu(self.fc1(x))
        x = leaky_relu(self.fc2(x))
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
