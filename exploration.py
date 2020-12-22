
from random import random
from torch.nn.functional import softmax
from numpy.random import choice
from Utils.server import isServer


class Exploration():
    def __init__(self) -> None:
        self.counter = 1

    @property
    def epsilon(self):
        K = 10000000 if isServer else 1000000
        return max(0.1, 1 - self.counter / K)

    @property
    def K(self):
        C = 500000 if isServer else 50000
        return max(0.01, C / self.counter)

    def softmax(self, vals):
        self.counter += 1
        if self.counter % 1000 == 1:
            print(f"({str(float(vals.max()))[:4]}, {str(float(vals.std()))[:4]})", end=", ")
        return int(choice(15, 1, p=softmax(vals / self.K, dim=0).detach().cpu().numpy()))

    def greedy(self, vals):
        self.counter += 1
        # if self.counter % 1000 == 1:
        #    print(f"({str(float(vals.max()))[:4]}, {str(float(vals.std()))[:4]})", end=", ")
        return vals.detach().cpu().numpy().argmax()

    def epsilonGreedy(self, vals):
        self.counter += 1
        if self.counter % 1000000 == 1:
            print(f"({str(float(vals.max()))[:4]}, {str(float(vals.std()))[:4]})", end=", ")
        return int(choice(15, 1)) if random() < self.epsilon else vals.detach().cpu().numpy().argmax()

    def epsintosoftmax(self, vals):
        self.counter += 1
        if self.counter % 1000000 == 1:
            print(f"({str(float(vals.max()))[:4]}, {str(float(vals.std()))[:4]})", end=", ")
        return int(choice(15, 1)) if random() < self.epsilon else int(choice(15, 1, p=softmax(vals / self.K, dim=0).detach().cpu().numpy()))

