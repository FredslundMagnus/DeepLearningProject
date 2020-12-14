"""
[1] https://www.element61.be/en/resource/quick-guide-reinforcement-learning-and-how-experiment-using-openai-gym
"""


from torch.nn import Module, Conv2d, MaxPool2d, Linear, MSELoss, LSTM, LeakyReLU, Sequential, ReLU, Sigmoid
from torch.optim import Adam, SGD
from memory import ReplayBuffer
from exploration import Exploration
import torch
from helpers import device, hidden_size, count_parameters
from torch import cat as concatenation, float32
import pickle


class Agent:
    def __init__(self, exploration='epsilonGreedy', memory=10000, discount=0.99, uncertainty=True, uncertainty_weight=1, update_every=200, double=True, use_distribution=True, reward_normalization=False, encoder=None, hidden_size=40, state_difference=True, state_difference_weight=1, **kwargs) -> None:
        self.uncertainty = uncertainty
        self.hidden_size = hidden_size
        self.network = NetWork(self.hidden_size).to(device)
        self.createEncoder(encoder)
        self.network.hasEncoder = self.hasEncoder
        print("Number of parameters in network:", count_parameters(self.network))
        self.criterion = MSELoss()
        self.memory = ReplayBuffer(int(memory))
        self.remember = self.memory.remember()
        self.exploration = Exploration()
        if exploration == 'greedy':
            self.explore = self.exploration.greedy
        elif exploration == 'epsilonGreedy':
            self.explore = self.exploration.epsilonGreedy
        elif exploration == 'softmax':
            self.explore = self.exploration.softmax
        elif exploration == 'epsintosoftmax':
            self.explore = self.exploration.epsintosoftmax
        self.target_network = NetWork(self.hidden_size).to(device)
        self.target_network.hasEncoder = self.hasEncoder
        self.placeholder_network = NetWork(self.hidden_size).to(device)
        self.placeholder_network.hasEncoder = self.hasEncoder
        self.gamma, self.f = discount, 0
        self.update_every, self.double, self.use_distribution = update_every, double, use_distribution
        self.counter = 0
        self.reward_normalization = reward_normalization
        self.state_difference = state_difference
        self.true_state_trace = None
        self.uncertainty_weight = uncertainty_weight
        self.state_difference_weight = state_difference_weight
        if encoder is not None:
            self.optimizer_value = Adam(list(self.network.fromEncoder.parameters()) + list(self.network.lstm.parameters()) + list(self.network.linear.parameters()), lr=1e-4, weight_decay=1e-5)
        else:
            self.optimizer_value = Adam(list(self.network.color.parameters()) + list(self.network.conv1.parameters()) + list(self.network.lstm.parameters()) + list(self.network.linear.parameters()), lr=1e-4, weight_decay=1e-5)
        if self.uncertainty:
            self.optimizer_exploration = Adam(list(self.network.exploration_network.parameters()), lr=1e-5, weight_decay=1e-5)
        if self.state_difference:
            self.optimizer_state_avoidance = Adam(list(self.network.state_difference_network.parameters()), lr=1e-6, weight_decay=1e-5)
        self.onpolicy = True

    def rememberMulti(self, *args):
        done = 1 - torch.tensor(list(args[8])).type(torch.float)
        if self.true_state_trace is not None:
            self.true_state_trace = (done.to(device) * (self.true_state_trace.transpose(0, 2))).transpose(0, 2)
        [self.remember(obs_old.cpu(), act, obs.cpu(), rew, h0.detach().cpu(), c0.detach().cpu(), hn.detach().cpu(), cn.detach().cpu(), int(not done)) for obs_old, act, obs, rew, h0, c0, hn, cn, done in zip(*args)]

    def choose(self, pixels, hn, cn):
        self.network.hn, self.network.cn = hn, cn
        vals, uncertainty = self.network(pixels)
        vals.reshape(15)
        return self.explore(vals, uncertainty), pixels, hn, cn, self.network.hn, self.network.cn

    def chooseMulti(self, pixels, hn, cn, lambda_decay=0.95, avoid_trace=0):
        self.network.hn, self.network.cn = concatenation(hn, 1).to(device), concatenation(cn, 1).to(device)
        vals, uncertainties, _, true_state = self.network(concatenation(pixels, 0).to(device))
        if self.onpolicy:
            return [val.reshape(15).detach().cpu().numpy().argmax() for val in torch.split(vals, 1)], pixels, hn, cn, torch.split(self.network.hn, 1, dim=1), torch.split(self.network.cn, 1, dim=1)
        if self.state_difference:
            if self.true_state_trace is None:
                self.true_state_trace = true_state.detach()
            else:
                self.true_state_trace = self.true_state_trace * lambda_decay + true_state * (1 - lambda_decay)
            avoid_trace = self.network.avoid_similar_state(self.true_state_trace)[0]
        vals = self.convert_values(vals, uncertainties, avoid_trace)
        return [self.explore(val.reshape(15)) for val in torch.split(vals, 1)], pixels, hn, cn, torch.split(self.network.hn, 1, dim=1), torch.split(self.network.cn, 1, dim=1)

    def learn(self):
        self.f += 1
        if self.f % self.update_every == 0:
            self.update_target_network()
            if self.reward_normalization:
                self.memory.average_reward()
        if self.f % 50000 > 48000:
            self.onpolicy = True
            return
        else:
            self.onpolicy = False
        if self.f > self.update_every:
            for _ in range(1):
                self.TD_learn()

    def TD_learn(self):
        obs, action, obs_next, reward, h0, c0, hn, sn, done = self.memory.sample_distribution(256) if self.use_distribution else self.memory.sample(256)
        self.network.hn, self.network.cn, self.target_network.hn, self.target_network.cn = hn, sn, hn, sn
        vals_target, uncertainties_target, state_differences_target, true_state_target = self.target_network(obs_next)

        if self.double:
            v_s_next = torch.gather(vals_target, 1, torch.argmax(vals_target, 1).view(-1, 1)).squeeze(1)
        else:
            v_s_next, _ = torch.max(vals_target, 1)

        if self.uncertainty:
            if self.double:
                uncer_next = torch.gather(uncertainties_target, 1, torch.argmax(uncertainties_target, 1).view(-1, 1)).squeeze(1)
            else:
                uncer_next, _ = torch.max(uncertainties_target, 1)
        if self.state_difference:
            if self.double:
                state_next = torch.gather(state_differences_target, 1, torch.argmax(state_differences_target, 1).view(-1, 1)).squeeze(1)
            else:
                state_next, _ = torch.max(state_differences_target, 1)

        self.network.hn, self.network.cn = h0, c0
        vals, uncertainties, state_differences, true_state = self.network(obs)
        vs = torch.gather(vals, 1, action)
        td = (reward + self.gamma * v_s_next * done.type(torch.float)).detach().view(-1, 1)

        if self.uncertainty:
            estimate_uncertainties = torch.gather(uncertainties, 1, action)
            reward_uncertainty = (abs(vs - td)).detach().view(-1)
            td_uncertainty = (reward_uncertainty + self.gamma * uncer_next * done.type(torch.float)).detach().view(-1, 1)
            loss_uncertainty = self.criterion(estimate_uncertainties, td_uncertainty)
            loss_uncertainty.backward(retain_graph=True)
            self.optimizer_exploration.step()
            self.optimizer_exploration.zero_grad()
        if self.state_difference:
            estimate_state_difference = (torch.gather(state_differences, 1, action).view(-1) * done.type(torch.float)).view(-1, 1)
            reward_state_difference = ((torch.sum((true_state_target - true_state)**2, dim=2)).view(-1)**(1 / 2) * done.type(torch.float)).view(-1)
            td_state_difference = (reward_state_difference + self.gamma * state_next * done.type(torch.float)).detach().view(-1, 1)
            loss_state_avoidance = self.criterion(estimate_state_difference, td_state_difference)
            loss_state_avoidance.backward(retain_graph=True)
            self.optimizer_state_avoidance.step()
            self.optimizer_state_avoidance.zero_grad()

        loss_value_network = self.criterion(vs, td)
        loss_value_network.backward()
        self.optimizer_value.step()
        self.optimizer_value.zero_grad()

        # torch.cuda.empty_cache()

    def convert_values(self, vals, uncertainties, state_differences):
        if self.f % 100 == 0:
            print([int(x) / 100 for x in 100 * vals[0].cpu().detach().numpy()])
            print([int(x) / 100 for x in 100 * uncertainties[0].cpu().detach().numpy()])
            print([int(x) / 100 for x in 100 * state_differences[0].cpu().detach().numpy()])
            print(" ")
        return vals + (float(self.uncertainty_weight) * uncertainties * float(self.uncertainty)) + (float(self.state_difference_weight) * state_differences * float(self.state_difference))

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
    def __init__(self, h):
        self.size_after_conv = 128
        self.hidden_size = h
        self.current_state = None

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
            Conv2d(in_channels=12, out_channels=32, kernel_size=4, stride=1),
            LeakyReLU(),
            Conv2d(in_channels=32, out_channels=64, kernel_size=4, stride=1),
            LeakyReLU(),
            Conv2d(in_channels=64, out_channels=self.size_after_conv, kernel_size=4, stride=1),
            LeakyReLU(),
        )

        self.lstm = LSTM(self.size_after_conv, self.hidden_size, 1)

        self.linear = Sequential(
            LeakyReLU(),
            Linear(self.hidden_size, 15),
        )

        self.exploration_network = Sequential(
            LeakyReLU(),
            Linear(self.hidden_size, self.hidden_size),
            LeakyReLU(),
            Linear(self.hidden_size, self.hidden_size // 2),
            LeakyReLU(),
            Linear(self.hidden_size // 2, 15),
        )

        self.state_difference_network = Sequential(
            Linear(self.size_after_conv, self.size_after_conv),
            LeakyReLU(),
            Linear(self.size_after_conv, self.hidden_size),
            LeakyReLU(),
            Linear(self.hidden_size, 15),
        )

    def forward(self, x):
        self.lstm.flatten_parameters()
        if self.hasEncoder:
            x = self.fromEncoder(x)
        else:
            x = self.color(x)
            x = self.conv1(x)
        x = x.view(1, -1, self.size_after_conv)

        p = x.view(-1, 1, self.size_after_conv)
        z = x.view(-1, self.size_after_conv)
        z = self.state_difference_network(z.detach())
        x, (self.hn, self.cn) = self.lstm(x, (self.hn, self.cn))
        x = x.view(-1, self.hidden_size)
        y = self.exploration_network(x.detach())
        x = self.linear(x)
        return x, y, z, p.detach()

    def avoid_similar_state(self, x):
        return self.state_difference_network(x)
