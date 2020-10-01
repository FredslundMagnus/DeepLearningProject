"""
[1] https://www.element61.be/en/resource/quick-guide-reinforcement-learning-and-how-experiment-using-openai-gym
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from memory import ReplayBuffer
import time


class Agent:
    def __init__(self) -> None:
        self.network = NetWork()
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.network.parameters(), lr=3e-4, weight_decay=1e-5)
        self.memory = ReplayBuffer(1000)

    def choose(self, obs):
        result = NetWork(obs)
        return "action"

    def learn(self):
        pass

    def remember(self, *args):
        if len(self.memory) < self.memory.size:
            self.memory.append(*args)
        else:
            self.remember = self.memory.appendFast(self.memory.size, self.memory.memory)
            self.remember(*args)


# Example network from week 5
class NetWork(nn.Module):
    def __init__(self):
        super(NetWork, self).__init__()

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


agent = Agent()
start = time.time()
for i in range(5000000):
    agent.remember(1, 2, 3, 4)
end = time.time()
print(end - start)
