from typing import Iterator


class RunningList():
    __slots__ = ("list", "n", "pos", "_sum")

    def __init__(self, n):
        super().__init__()
        self.n = n
        self.clear()

    def clear(self):
        """Remove all items from list."""
        self.pos = 0
        self.list = []
        self._sum = 0

    def sum(self) -> float:
        return self._sum

    def mean(self) -> float:
        return self._sum / min(self.n, self.pos)

    @property
    def _k(self):
        return self.pos % self.n

    def append(self, number: float):
        """Append number to the end of the list."""
        if self.pos < self.n:
            self.list.append(number)
            self._sum += number
        else:
            self._sum += number - self.list[self._k]
            self.list[self._k] = number
        self.pos += 1

    def __repr__(self):
        return str(self.list[self._k:] + self.list[:self._k])

    def extend(self, iterable: Iterator[float]):
        """Extend list by appending numbers from the iterable."""
        for n in iterable:
            self.append(n)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, index):
        if index >= self.n:
            raise IndexError
        if index < -self.n:
            raise IndexError
        return self.list[(index + self._k) % self.n]
