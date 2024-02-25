class Cycle:
    def __init__(self, iterable):
        self.obj = iterable
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            val = self.obj[self.ind]
            self.ind += 1
            return val
        except:
            self.ind = 0
            val = self.obj[self.ind]
            self.ind += 1
            return val


if __name__ == '__main__':
    cycle = Cycle('be')

    print(next(cycle))
    print(next(cycle))
    print(next(cycle))
    print(next(cycle))
