class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        if self.start < self.end:
            self.a = True
        else:
            self.a = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.a:
            while self.start < self.end:
                v = self.start
                self.start += self.step
                return v
            else:
                raise StopIteration
        elif not self.a:
            while self.start > self.end:
                v = self.start
                self.start += self.step
                return v
            else:
                raise StopIteration


if __name__ == '__main__':
    xrange = Xrange(-20, 12, 4)

    print(*xrange)