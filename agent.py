"""
[1] https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html
[2] https://www.element61.be/en/resource/quick-guide-reinforcement-learning-and-how-experiment-using-openai-gym
"""

from collections import namedtuple
import torch
import random
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class Agent:
    def __init__(self) -> None:
        self.network = NetWork()
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.network.parameters(), lr=3e-4, weight_decay=1e-5)
        self.memory = ReplayMemory(1000)

    def choose(self, obs):
        result = NetWork(obs)
        return "action"

    def learn(self):
        pass

    def remember(self, state, action, next_state, reward, done):
        self.memory.push(state, action, next_state, reward)


# Example network from week 5
class NetWork(nn.Module):
    def __init__(self):
        super(Agent, self).__init__()

        # Recurrent layer
        # YOUR CODE HERE!
        self.lstm = nn.LSTM(input_size=50,
                            hidden_size=10,
                            num_layers=1,
                            bidirectional=False)

        # Output layer
        self.l_out = nn.Linear(in_features=10,
                               out_features=50,
                               bias=False)

    def forward(self, x):
        # RNN returns output and last hidden state
        x, (h, c) = self.lstm(x)

        # Flatten output for feed-forward layer
        x = x.view(-1, self.lstm.hidden_size)

        # Output layer
        x = self.l_out(x)

        return x


# [1]
Transition = namedtuple('Transition', ('state', 'action', 'next_state', 'reward'))


class ReplayMemory(object):
    # [1]
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
        self.position = 0

    def push(self, *args):
        """Saves a transition."""
        if len(self.memory) < self.capacity:
            self.memory.append(None)
        self.memory[self.position] = Transition(*args)
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)
