class Alphabet:
    def __init__(self, language):
        self.cod = language

        def func(self):
            if self.cod == 'en':
                self.ind = 97
                self.start = 97
                res = range(97, 123)
            elif self.cod == 'ru':
                self.ind = 1072
                self.start = 1072
                res = range(1072, 1104)
            return res

        self.res = func(self)

    def __iter__(self):
        return self

    def __next__(self):

        if self.ind in self.res:
            val = chr(self.ind)
            self.ind += 1
        else:
            self.ind = self.start
            val = chr(self.ind)
            self.ind += 1
        return val


if __name__ == '__main__':

    ru_alpha = Alphabet('ru')

    print(next(ru_alpha))
    print(next(ru_alpha))
    print(next(ru_alpha))
