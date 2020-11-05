import random
from helpers import stack
import numpy as np


class ReplayBuffer:
    def __init__(self, size: int) -> None:
        self.reset(size)

    def remember(self):
        size, memory, rewads, dones = self.size, self.memory, self.rewads, self.dones

        def inner(*args):
            memory[self.position % size] = args
            rewads[self.position % size] = args[3]
            dones[self.position % size] = args[8]
            self.position += 1
            return args[2]
        return inner

    def sample(self, batch_size: int):
        l = len(self)
        return stack(random.sample(self.memory[:l], min(batch_size, l)))

    def sample_distribution(self, batch_size: int):
        return stack([self.memory[i] for i in list(np.random.choice(len(self.distribution), batch_size, p=self.distribution))])

    def update_distribution(self, a=1, b=1, sigma=0.9, k=20):
        l = len(self)
        temp = np.absolute(np.array(self.rewads[:l] + [0] * k)) * a + b - np.array(self.dones[:l] + [1] * k) * b + 1
        temp_of_temp = temp.copy()
        for i in range(1, k):
            temp[:l] += temp_of_temp[i:l + i] * (sigma ** i)
        self.distribution = temp[:l] / temp[:l].sum()

    def __len__(self):
        return min(self.position, self.size)

    def __repr__(self):
        _k = self.position % self.size
        return str(self.memory[_k:len(self)] + self.memory[:_k])

    def reset(self, size: int):
        self.size, self.position, self.memory, self.rewads, self.dones, self.distribution = size, 0, [None for _ in range(size)], [None for _ in range(size)], [None for _ in range(size)], None
