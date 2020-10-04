import random
from helpers import stack


class ReplayBuffer:
    def __init__(self, size: int) -> None:
        self.size, self.position, self.memory = size, 0, [None for _ in range(size)]

    def remember(self):
        size, memory = self.size, self.memory

        def inner(*args):
            memory[self.position % size] = args
            self.position += 1
            return args[2]
        return inner

    def sample(self, batch_size: int):
        l = len(self)
        return stack(random.sample(self.memory[:l], min(batch_size, l)))

    def __len__(self):
        return min(self.position, self.size)

    def __repr__(self):
        _k = self.position % self.size
        return str(self.memory[_k:len(self)] + self.memory[:_k])
