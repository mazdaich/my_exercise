from abc import ABC, abstractmethod


class Paragraph(ABC):

    def __init__(self, length):
        self.length = length
        self.par = []
        self.lst = []

    # abstractmethod
    def add(self):
        pass

    # abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):
    def add(self, word):
        r = word.split()
        for i in r:
            if len(' '.join(self.lst)) + len(i + ' ') <= self.length:
                self.lst.append(i)
            else:
                self.lst = []
                self.lst.append(i)
            if self.lst not in self.par:
                self.par.append(self.lst)

    def end(self):
        for i in self.par:
            print(*i)
        self.par = []
        self.lst = []


class RightParagraph(Paragraph):
    def add(self, word):
        r = word.split()
        for i in r:
            if len(' '.join(self.lst)) + len(i + ' ') <= self.length:
                self.lst.append(i)
            else:
                self.lst = []
                self.lst.append(i)
            if self.lst not in self.par:
                self.par.append(self.lst)

    def end(self):
        for i in self.par:
            r = ' '.join(i)
            n = self.length - len(r)
            print(' ' * n + r)
        self.par = []
        self.lst = []


if __name__ == '__main__':

    rightparagraph = RightParagraph(28)

    rightparagraph.add('I will not regret the roses')
    rightparagraph.add('Withered with a light spring')
    rightparagraph.add('I love the grapes on the vines')
    rightparagraph.add('Ripened in the hands under the mountain')
    rightparagraph.end()

    rightparagraph.add('The beauty of my green valley')
    rightparagraph.add('Golden joy of autumn')
    rightparagraph.add('oblong and transparent')
    rightparagraph.add('Like the fingers of a young maiden')
    rightparagraph.end()
