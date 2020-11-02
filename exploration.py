
from random import random
from torch.nn.functional import softmax
from numpy.random import choice


class Exploration():
    def __init__(self) -> None:
        self.K = 0.05
        self.epsilon = 0.05

    def softmax(self, vals):
        print(f"({str(float(vals.max()))[:4]}, {str(float(vals.var()))[:4]})", end=", ")
        # print(vals)
        return int(choice(15, 1, p=softmax(vals / self.K, dim=0).detach().cpu().numpy()))

    def greedy(self, vals):
        return vals.detach().cpu().numpy().argmax()

    def epsilonGreedy(self, vals):
        print(f"({str(float(vals.max()))[:4]}, {str(float(vals.var()))[:4]})", end=", ")
        return int(choice(15, 1)) if random() < self.epsilon else vals.detach().cpu().numpy().argmax()
