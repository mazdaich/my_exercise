from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        lst = []
        for i in args:
            if isinstance(i, int):
                lst.append(i)
            if isinstance(i, str):
                r = i.split('-')
                lst += (range(int(r[0]), int(r[-1]) + 1))
        self.lst = lst

    def __len__(self):

        return len(self.lst)

    def __getitem__(self, index):
        return self.lst[index]


if __name__ == '__main__':

    customrange = CustomRange(1, '2-5', 3, '1-4')

    print(*customrange)
    print(*reversed(customrange))
    print(len(customrange))
    print(1 in customrange)
    print(10 in customrange)
