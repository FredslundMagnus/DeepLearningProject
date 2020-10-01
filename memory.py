import random
from typing import List


class Transition:
    __slots__ = 'state', 'action', 'next_state', 'reward'

    def __init__(self, args) -> None:
        self.state, self.action, self.next_state, self.reward = args

    def __repr__(self):
        return f"Transition(state{self.state.shape}, {self.action}, next_state{self.next_state.shape}, {self.reward})"


class ReplayBuffer:
    def __init__(self, size: int) -> None:
        self.size, self.position, self.memory = size, 0, [None for _ in range(size)]

    def remember(self):
        size, memory = self.size, self.memory

        def inner(*args):
            memory[self.position % size] = Transition(args)
            self.position += 1
        return inner

    def sample(self, batch_size: int) -> List[Transition]:
        l = len(self)
        return random.sample(self.memory[:l], min(batch_size, l))

    def __len__(self):
        return min(self.position, self.size)

    def __repr__(self):
        _k = self.position % self.size
        return str(self.memory[_k:len(self)] + self.memory[:_k])
