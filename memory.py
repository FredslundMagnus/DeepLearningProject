import random


class Transition:
    __slots__ = ('state', 'action', 'next_state', 'reward')

    def __init__(self, *args) -> None:
        self.state, self.action, self.next_state, self.reward = tuple(*args)

    def __repr__(self):
        return f"Transition({self.state}, {self.action}, {self.next_state}, {self.reward})"


class ReplayBuffer:
    def __init__(self, size):
        self.size = size
        self.position = 0
        self.memory = []

    def append(self, *args):
        self.memory.append(Transition(args))
        self.position += 1

    def appendFast(self, size, memory):
        def inner(*args):
            memory[self.position % size] = Transition(args)
            self.position += 1
        return inner

    def sample(self, batch_size):
        return random.sample(self.memory, min(batch_size, len(self)))

    def __len__(self):
        return len(self.memory)

    def __getitem__(self, index):
        return self.memory[(index + self.position) % self.size]

    def __repr__(self):
        _k = self.position % self.size
        return str(self.memory[_k:] + self.memory[:_k])
