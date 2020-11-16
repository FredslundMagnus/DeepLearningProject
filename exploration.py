
from random import random
from torch.nn.functional import softmax
from numpy.random import choice


class Exploration():
    def __init__(self) -> None:
        self.counter = 1

    @property
    def epsilon(self):
        return max(0.1, 1 - self.counter / 1000000)

    @property
    def K(self):
        return max(0.005, 5000 / self.counter)

    def softmax(self, vals):
        self.counter += 1
        if self.counter % 1000 == 1:
            print(f"({str(float(vals.max()))[:4]}, {str(float(vals.std()))[:4]})", end=", ")
        return int(choice(15, 1, p=softmax(vals / self.K, dim=0).detach().cpu().numpy()))

    def greedy(self, vals):
        self.counter += 1
        if self.counter % 1000 == 1:
            print(f"({str(float(vals.max()))[:4]}, {str(float(vals.std()))[:4]})", end=", ")
        return vals.detach().cpu().numpy().argmax()

    def epsilonGreedy(self, vals):
        self.counter += 1
        if self.counter % 1000 == 1:
            print(f"({str(float(vals.max()))[:4]}, {str(float(vals.std()))[:4]})", end=", ")
        return int(choice(15, 1)) if random() < self.epsilon else vals.detach().cpu().numpy().argmax()

    def EpsilonSoftmaxUncertainty(self, vals):
        self.counter += 1
        uncertainty = vals[-1]
        vals = vals[:-1]
        weight = 1 # High means more uncertain (0 is just a greedy policy)
        K = uncertainty * weight
        if self.counter % 200 == 1:
            print(f"({str(float(vals.max()))[:4]}, {str(float(vals.std()))[:4]}, {str(float(uncertainty))[:4]})", end=", ")
        return int(choice(15, 1, p=softmax(vals / K, dim=0).detach().cpu().numpy())) if K > 1e-5 else vals.detach().cpu().numpy().argmax()
