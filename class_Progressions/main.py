class ArithmeticProgression:
    def __init__(self, start, step):
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        return self.start - self.step


class GeometricProgression:
    def __init__(self, start, step):
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        r = self.start
        self.start *= self.step
        return r


if __name__ == '__main__':
    progression = ArithmeticProgression(0, 1)

    for elem in progression:
        if elem > 10:
            break
        print(elem, end=' ')

    progression = GeometricProgression(1, 2)

    for elem in progression:
        if elem > 10:
            break
        print(elem, end=' ')
