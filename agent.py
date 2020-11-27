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
    def __init__(self, exploration='greedy', memory=10000, discount=0.995, uncertainty=True, update_every=200, double=True, use_distribution=True, reward_normalization=True, **kwargs) -> None:
        self.uncertainty = uncertainty
        self.network = NetWork().to(device)
        self.createEncoder(encoder)
        self.network.hasEncoder = self.hasEncoder
        print("Number of parameters in network:", count_parameters(self.network))
        self.criterion = MSELoss()
        self.optimizer = Adam(self.network.parameters(), lr=1e-4, weight_decay=1e-5)
        self.memory = ReplayBuffer(int(memory))
        self.remember = self.memory.remember()
        self.exploration = Exploration()
        if exploration == 'greedy':
            self.explore = self.exploration.greedy
        elif exploration == 'epsilonGreedy':
            self.explore = self.exploration.epsilonGreedy
        elif exploration == 'softmax':
            self.explore = self.exploration.softmax
        elif exploration == 'greedyintosoftmax':
            self.explore = self.exploration.greedyintosoftmax

        self.target_network = NetWork().to(device)
        self.target_network.hasEncoder = self.hasEncoder
        self.placeholder_network = NetWork().to(device)
        self.placeholder_network.hasEncoder = self.hasEncoder
        self.gamma, self.f = discount, 0
        self.update_every, self.double, self.use_distribution = update_every, double, use_distribution
        self.counter = 0
        self.reward_normalization = reward_normalization

    def rememberMulti(self, *args):
        [self.remember(obs_old.cpu(), act, obs.cpu(), rew, h0.detach().cpu(), c0.detach().cpu(), hn.detach().cpu(), cn.detach().cpu(), int(not done)) for obs_old, act, obs, rew, h0, c0, hn, cn, done in zip(*args)]

    def choose(self, pixels, hn, cn):
        self.network.hn, self.network.cn = hn, cn
        vals, uncertainty = self.network(pixels)
        vals.reshape(15)
        return self.explore(vals, uncertainty), pixels, hn, cn, self.network.hn, self.network.cn

    def chooseMulti(self, pixels, hn, cn):
        self.network.hn, self.network.cn = concatenation(hn, 1).to(device), concatenation(cn, 1).to(device)
        vals, uncertainties = self.network(concatenation(pixels, 0).to(device))
        vals = self.convert_uncertainty_values(vals, uncertainties)
        return [self.explore(val.reshape(15)) for val in torch.split(vals, 1)], pixels, hn, cn, torch.split(self.network.hn, 1, dim=1), torch.split(self.network.cn, 1, dim=1)

    def learn(self):
        self.f += 1
        if self.f % self.update_every == 0:
            self.update_target_network()
            if self.reward_normalization:
                self.memory.average_reward()
        if self.f > self.update_every:
            for _ in range(1):
                self.TD_learn()

    def TD_learn(self):
        obs, action, obs_next, reward, h0, c0, hn, sn, done = self.memory.sample_distribution(256) if self.use_distribution else self.memory.sample(256)
        self.network.hn, self.network.cn, self.target_network.hn, self.target_network.cn = hn, sn, hn, sn
        if self.double:
            v_s_next = torch.gather(self.target_network(obs_next)[0], 1, torch.argmax(self.network(obs_next)[0], 1).view(-1, 1)).squeeze(1)
        else:
            v_s_next, input_indexes = torch.max(self.target_network(obs_next)[0], 1)
        self.network.hn, self.network.cn = h0, c0
        output_this_state = self.network(obs)
        vs = torch.gather(output_this_state[0], 1, action)
        td = ((reward - self.memory.reward_avg) / self.memory.reward_std + self.gamma * v_s_next * done.type(torch.float)).detach().view(-1, 1)

        if self.uncertainty:
            estimate_uncertainties = torch.gather(output_this_state[1], 1, action)
            true_uncertainty = abs(td - vs.detach())
            guess = torch.cat((vs, estimate_uncertainties), 1)
            label = torch.cat((td, true_uncertainty), 1)
            loss = self.criterion(guess, label)
        else:
            loss = self.criterion(vs, td)

        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

        # torch.cuda.empty_cache()

    def convert_uncertainty_values(self, vals, uncertainties):
        if self.uncertainty:
            return vals + uncertainties / 2
        else:
            return vals

    def update_target_network(self):
        self.target_network = pickle.loads(pickle.dumps(self.placeholder_network))
        self.placeholder_network = pickle.loads(pickle.dumps(self.network))
        self.memory.update_distribution()

    def createEncoder(self, encoder):
        if encoder:
            with open(f"Encoders/{encoder}.obj", "rb") as file:
                self.encoder = pickle.load(file).encoder.to(device)
                self.hasEncoder = True
        else:
            self.hasEncoder = False


class NetWork(Module):
    def __init__(self):
        self.size_after_conv = 128

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
            Conv2d(in_channels=12, out_channels=32, kernel_size=4, stride=2),
            LeakyReLU(),
            Conv2d(in_channels=32, out_channels=self.size_after_conv, kernel_size=4, stride=1),
            LeakyReLU(),
        )

        self.lstm = LSTM(self.size_after_conv, hidden_size, 1)

        self.linear = Sequential(
            LeakyReLU(),
            Linear(hidden_size, 15),
        )

        self.exploration_network = Sequential(
            LeakyReLU(),
            Linear(hidden_size, hidden_size/2),
            LeakyReLU(),
            Linear(hidden_size/2, hidden_size/2),
            LeakyReLU(),
            Linear(hidden_size/2, 15),
        )

    def forward(self, x):
        self.lstm.flatten_parameters()
        if self.hasEncoder:
            x = self.fromEncoder(x)
        else:
            x = self.color(x)
            x = self.conv1(x)
        x = x.view(1, -1, self.size_after_conv)
        x, (self.hn, self.cn) = self.lstm(x, (self.hn, self.cn))
        x = x.view(-1, hidden_size)
        y = x.clone()
        y = self.exploration_network(y.detach())
        x = self.linear(x)
        return x, y


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
