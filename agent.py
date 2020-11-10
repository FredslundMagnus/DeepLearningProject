"""
[1] https://www.element61.be/en/resource/quick-guide-reinforcement-learning-and-how-experiment-using-openai-gym
"""


from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU
from torch.optim import Adam
from memory import ReplayBuffer
from exploration import Exploration
import torch
from helpers import device, hidden_size, count_parameters
from torch import cat as concatenation
import pickle


class Agent:
    def __init__(self, memory=50000, discount=0.99, uncertainty=False) -> None:
        self.uncertainty = uncertainty
        self.network = NetWork(uncertainty=self.uncertainty).to(device)
        print("Number of parameters in network:", count_parameters(self.network))
        self.criterion = MSELoss()
        self.optimizer = Adam(self.network.parameters(), lr=5e-4, weight_decay=1e-5)
        self.memory = ReplayBuffer(memory)
        self.remember = self.memory.remember()
        self.exploration = Exploration()
        self.explore = self.exploration.EpsilonSoftmaxUncertainty if uncertainty else self.exploration.epsilonGreedy
        self.target_network = NetWork(uncertainty=self.uncertainty).to(device)
        self.placeholder_network = NetWork(uncertainty=self.uncertainty).to(device)
        self.gamma = discount

    def rememberMulti(self, *args):
        [self.remember(obs_old.cpu(), act, obs.cpu(), rew, h0.detach().cpu(), c0.detach().cpu(), hn.detach().cpu(), cn.detach().cpu(), int(not done)) for obs_old, act, obs, rew, h0, c0, hn, cn, done in zip(*args)]

    def choose(self, pixels, hn, cn):
        self.network.hn, self.network.cn = hn, cn
        vals, uncertainty = self.network(pixels)
        vals.reshape(15)
        return self.explore(vals, uncertainty), pixels, hn, cn, self.network.hn, self.network.cn

    def chooseMulti(self, pixels, hn, cn):
        self.network.hn, self.network.cn = concatenation(hn, 1).to(device), concatenation(cn, 1).to(device)
        vals = self.network(concatenation(pixels, 0).to(device))
        return [self.explore(val.reshape(15 + self.uncertainty)) for val in torch.split(vals, 1)], pixels, hn, cn, torch.split(self.network.hn, 1, dim=1), torch.split(self.network.cn, 1, dim=1)

    def learn(self, double=False, use_distribution=True):
        obs, action, obs_next, reward, h0, c0, hn, sn, done = self.memory.sample_distribution(256) if use_distribution else self.memory.sample(200)
        uncertainty_weighting = 1  # has to be between 0 and 1. 0 means no training is done towards uncertainty prediction.
        self.network.hn, self.network.cn, self.target_network.hn, self.target_network.cn = hn, sn, hn, sn
        if double:
            v_s_next = torch.gather(self.target_network(obs_next), 1, torch.argmax(self.network(obs_next)[:, :15], 1).view(-1, 1)).squeeze(1)
        else:
            v_s_next, input_indexes = torch.max(self.target_network(obs_next)[:, :15], 1)

        self.network.hn, self.network.cn = h0, c0
        output_this_state = self.network(obs)
        vs = torch.gather(output_this_state, 1, action)
        td = (reward + self.gamma * v_s_next * done.type(torch.float)).detach().view(-1, 1)
        if self.uncertainty:
            estimate_uncertainty = output_this_state[:, 15].view(-1, 1).clone()
            estimate_uncertainty[estimate_uncertainty < 0] = 0
            true_uncertainty = uncertainty_weighting * abs(td - vs) + (1 - uncertainty_weighting) * estimate_uncertainty
            guess = torch.cat((vs, estimate_uncertainty), 1)
            label = torch.cat((td, true_uncertainty.detach()), 1)
            loss = self.criterion(guess, label)
        else:
            loss = self.criterion(vs, td)
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
        # torch.cuda.empty_cache()

    def update_target_network(self):
        self.target_network = pickle.loads(pickle.dumps(self.placeholder_network))
        self.placeholder_network = pickle.loads(pickle.dumps(self.network))
        self.memory.update_distribution()


class NetWork(Module):
    def __init__(self, uncertainty):
        self.size_after_conv = 64

        super(NetWork, self).__init__()

        self.color = Sequential(Conv2d(in_channels=3, out_channels=32, kernel_size=6, stride=2),
                    LeakyReLU(),
                    Conv2d(in_channels=32, out_channels=64, kernel_size=4, stride=2),
                    MaxPool2d(2, 2, padding=0),
                    LeakyReLU(),
                    )
        self.conv1 = Sequential(
            Conv2d(in_channels=64, out_channels=64, kernel_size=4, stride=1),
            LeakyReLU(),
            Conv2d(in_channels=64, out_channels=128, kernel_size=4, stride=1),
            LeakyReLU(),
        )

        self.lstm = LSTM(self.size_after_conv, hidden_size, 1)
        self.linear = Sequential(LeakyReLU(),
                                 Linear(128, 15 + uncertainty),
                                 )

    def forward(self, x):
        self.lstm.flatten_parameters()
        x = self.color(x)
        x = self.conv1(x)
        #x = x.view(1, -1, self.size_after_conv)
        #x, (self.hn, self.cn) = self.lstm(x, (self.hn, self.cn))
        x = x.view(-1, 128)
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
