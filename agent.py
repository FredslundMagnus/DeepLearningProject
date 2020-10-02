"""
[1] https://www.element61.be/en/resource/quick-guide-reinforcement-learning-and-how-experiment-using-openai-gym
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from memory import ReplayBuffer


class Agent:
    def __init__(self) -> None:
        self.network = NetWork()
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.network.parameters(), lr=3e-4, weight_decay=1e-5)
        self.memory = ReplayBuffer(1000)
        self.remember = self.memory.remember()

    def choose(self, obs):
        result = self.network(torch.as_tensor(obs.transpose(2, 0, 1)).reshape(-1, 3, 64, 64).float())
        return result.detach().numpy().argmax()

    def learn(self):
        pass


class NetWork(nn.Module):
    def __init__(self):
        super(NetWork, self).__init__()

        self.conv1 = nn.Conv2d(in_channels=3, out_channels=10, kernel_size=3)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(in_channels=10, out_channels=20, kernel_size=3)
        self.size_after_conv = 3920
        self.fc1 = nn.Linear(self.size_after_conv, 120)
        self.fc2 = nn.Linear(120, 60)
        self.fc3 = nn.Linear(60, 15)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, self.size_after_conv)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
