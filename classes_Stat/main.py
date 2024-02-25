from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, it=[]):
        self.it = it

    def add(self, n):
        self.it.append(n)

    def clear(self):
        self.it = []

    # abstractmethod
    def result(self):
        pass


class MinStat(Stat):
    def result(self):
        if self.it:
            return min(self.it)
        return None


class MaxStat(Stat):
    def result(self):
        if self.it:
            return max(self.it)
        return None


class AverageStat(Stat):
    def result(self):
        if self.it:
            return sum(self.it) / len(self.it)
        return None


if __name__ == '__main__':

    minstat = MinStat([1, 2, 4])
    maxstat = MaxStat([1, 2, 4])
    averagestat = AverageStat([1, 2, 4])

    minstat.add(5)
    maxstat.add(5)
    averagestat.add(5)

    print(minstat.result())
    print(maxstat.result())
    print(averagestat.result())
