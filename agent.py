"""
https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html
"""
# Example network from week 5
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class Agent(nn.Module):
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
