from collections.abc import Sequence, Set

class BitArray(Set):
    def __init__(self, it=[]):
        self.lst = [i for i in it]
    def __invert__(self):
        return BitArray([0 if i else 1 for i in self.lst])
    def __len__(self):
        return len(self.lst)
    def __getitem__(self, index):
        return self.lst[index]
    def __repr__(self):
        return f'{self.lst}'
    def __contains__(self, n):
        return n in self.lst
    def __iter__(self):
        return iter(self.lst)
    def __or__(self, other):
        try:
            return BitArray(list(i[0] | i[1] for i in zip(self.lst, other)))
        except:
            return NotImplemented
    def __and__(self, other):
        try:
            return BitArray(list(i[0] & i[1] for i in zip(self.lst, other)))
        except:
            return NotImplemented


if __name__ == '__main__':
    bitarray = BitArray([1, 0, 1, 1])

    print(bitarray)
    print(~bitarray)
    print(bitarray[0])
    print(bitarray[1])
    print(bitarray[-1])
    print(0 in bitarray)
    print(1 not in bitarray)