
from torch.nn.functional import softmax
from numpy.random import choice


class Exploration():
    def __init__(self) -> None:
        self.K = 100

    def softmax(self, vals):
        return int(choice(15, 1, p=softmax(vals / self.K, dim=0).detach().cpu().numpy()))
