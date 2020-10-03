"""
[1] https://www.element61.be/en/resource/quick-guide-reinforcement-learning-and-how-experiment-using-openai-gym
"""

from torch import as_tensor
from torch.nn import Module, Conv2d, MaxPool2d, Linear, CrossEntropyLoss
from torch.nn.functional import relu
from torch.optim import Adam
from memory import ReplayBuffer
from exploration import Exploration


class Agent:
    def __init__(self) -> None:
        self.network = NetWork()
        self.criterion = CrossEntropyLoss()
        self.optimizer = Adam(self.network.parameters(), lr=3e-4, weight_decay=1e-5)
        self.memory = ReplayBuffer(1000)
        self.remember = self.memory.remember()
        self.exploration = Exploration()
        self.explore = self.exploration.softmax

    def choose(self, obs):
        vals = self.network(as_tensor(obs.transpose(2, 0, 1)).reshape(-1, 3, 64, 64).float()).reshape(15)
        return self.explore(vals)

    def learn(self):
        pass


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
