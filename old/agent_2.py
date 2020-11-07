"""
[1] https://www.element61.be/en/resource/quick-guide-reinforcement-learning-and-how-experiment-using-openai-gym
"""


from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU, Sigmoid, CrossEntropyLoss, BatchNorm2d
from torch.optim import Adam
from memory import ReplayBuffer
from exploration import Exploration
import torch
from helpers import device, hidden_size, count_parameters
import copy


class Clamp(Module):
    def __init__(self, min=0, max=1):
        super(Clamp, self).__init__()
        self.min = min
        self.max = max

    def forward(self, x):
        return torch.clamp(x, min=self.min, max=self.max)


class Agent:
    def __init__(self) -> None:
        self.network = NetWork().to(device)
        print("Number of parameters in network:", count_parameters(self.network))
        self.criterion = MSELoss()
        self.optimizer = Adam(self.network.parameters(), lr=0.001, weight_decay=0.001)
        self.memory = ReplayBuffer(100000)
        self.remember = self.memory.remember()
        self.exploration = Exploration()
        self.explore = self.exploration.epsilonGreedy
        self.target_network = NetWork().to(device)
        self.placeholder_network = NetWork().to(device)

    def choose(self, pixels, hn, cn):
        self.network.hn, self.network.cn = hn, cn
        vals = self.network(pixels).reshape(15)
        return self.explore(vals), pixels, hn, cn, self.network.hn, self.network.cn

    def learn(self, double=False):
        gamma = 0.96
        obs, action, obs_next, reward, h0, c0, hn, sn, done = self.memory.sample_distribution(20)
        # self.network.hn, self.network.cn = hn, sn

        # if double:
        #     v_s_next = torch.gather(self.target_network(obs_next), 1, torch.argmax(self.network(obs_next), 1).view(-1, 1)).squeeze(1)
        # else:
        #     v_s_next, input_indexes = torch.max(self.target_network(obs_next), 1)

        # self.network.hn, self.network.cn = h0, c0
        # v_s = torch.gather(self.network(obs), 1, action)
        # #v_s, _ = torch.max(self.network(obs), 1)
        # td = (reward + gamma * v_s_next * done.type(torch.float)).detach().view(-1, 1)
        # loss = self.criterion(v_s, td)
        # loss.backward()
        # self.optimizer.step()
        # self.optimizer.zero_grad()
        # torch.cuda.empty_cache()
        self.autoEncode(obs)

    def autoEncode(self, obs):
        enc = self.network.color(obs)
        obs_Guess = self.network.colorReverse(enc)
        # print(enc.prod(1).sum())

        # print(f"[{str(float(enc_stand.max()))[:8]}]", end=" ")
        entro = (enc + 1).prod(1) - (1 + enc).max(1)[0]
        img = self.criterion(obs_Guess.view(20, -1), obs.view(20, -1) / 256)
        # print(enc.max(1)[0].max(1)[0].max(1)[0].shape)
        # print(enc.max(1, keepdim=True)[0].shape)
        maxi = enc.max(1, keepdim=False)[0]
        loss = img * 100 + (entro * entro).mean()
        loss.backward()

        self.optimizer.step()
        self.optimizer.zero_grad()
        print(f"[{str(float(loss))[:8]}]", end=" ")
        print(f"[{str(float(img*100))[:8]}]", end=" ")
        print(f"[{str(float((entro * entro).mean()))[:8]}]", end=" ")
        print(f"[{str(float(enc.min()))[:8]}]", end=" ")
        print(f"[{str(float(enc.max()))[:8]}]")
        # print(f"[{str(float(enc.mean()))[:8]}]")
        # print(f"[{str(float(entro.min()))[:8]}]", end=" ")
        # print(f"[{str(float(entro.max()))[:8]}]", end=" ")
        # print(f"[{str(float(enc.max()))[:8]}]")
       # print(*[[float(str(f)[:5]) for f in list(p.detach().cpu().numpy().reshape(-1))] for p in self.network.color.parameters()], *[[float(str(f)[:5]) for f in list(p.detach().cpu().numpy().reshape(-1))] for p in self.network.colorReverse.parameters()])
        torch.cuda.empty_cache()

    def update_target_network(self):
        self.target_network = copy.deepcopy(self.placeholder_network)
        self.placeholder_network = copy.deepcopy(self.network)
        self.memory.update_distribution()


class NetWork(Module):
    def __init__(self):
        super(NetWork, self).__init__()

        # self.normalise = BatchNorm2d(3)
        colors = 9
        self.color = Sequential(BatchNorm2d(3), Conv2d(in_channels=3, out_channels=5, kernel_size=1), ReLU(), Conv2d(in_channels=5, out_channels=colors, kernel_size=1), Sigmoid())

        self.colorReverse = Sequential(Conv2d(in_channels=colors, out_channels=5, kernel_size=1), ReLU(), Conv2d(in_channels=5, out_channels=3, kernel_size=1))

        self.conv1 = Sequential(
            Conv2d(in_channels=colors, out_channels=5, kernel_size=5, stride=2),
            LeakyReLU(),
            Conv2d(in_channels=5, out_channels=5, kernel_size=5, stride=2),
            LeakyReLU(),
            Conv2d(in_channels=5, out_channels=5, kernel_size=4, stride=2),
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
            Linear(125, 30),
            # Linear(hidden_size, 40),
            LeakyReLU(),
            Linear(30, 15),
        )

    def forward(self, x):
        # x = self.normalise(x)
        x = self.color(x)
        x = self.conv1(x)
        #x = self.conv2(x)
        #x = self.conv3(x)

        # x = x.view(1, -1, self.size_after_conv)
        # x, (self.hn, self.cn) = self.lstm(x, (self.hn, self.cn))
        # x = x.view(-1, hidden_size)
        x = x.view(-1, 125)
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
