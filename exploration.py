
from random import random
from torch.nn.functional import softmax
from numpy.random import choice


class Exploration():
    def __init__(self) -> None:
        self.counter = 1

    @property
    def K(self):
        return max(0.005, 5000 / self.counter)

    @property
    def epsilon(self):
        return max(0.05, 1 - self.counter / 1000000)

    def softmax(self, vals, uncertainty=1):
        self.counter += 1
        if self.counter % 1000 == 0:
            print(f"({str(float(vals.max()))[:4]}, {str(float(vals.std()))[:4]})", end=", ")
        return int(choice(15, 1, p=softmax(vals / self.K, dim=0).detach().cpu().numpy()))

    def greedy(self, vals, uncertainty=1):
        if self.counter % 1000 == 0:
            print(f"({str(float(vals.max()))[:4]}, {str(float(vals.std()))[:4]})", end=", ")
        return vals.detach().cpu().numpy().argmax()

    def epsilonGreedy(self, vals, uncertainty=1):
        self.counter += 1
        if self.counter % 1000 == 0:
            print(f"({str(float(vals.max()))[:4]}, {str(float(vals.std()))[:4]})", end=", ")
        return int(choice(15, 1)) if random() < self.epsilon else vals.detach().cpu().numpy().argmax()
