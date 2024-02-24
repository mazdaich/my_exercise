from math import sqrt


class Vector:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return str(self.args)

    def len_test(self, other):
        if not len(self.args) == len(other.args):
            raise ValueError('Векторы должны иметь равную длину')

    def __add__(self, other):
        self.len_test(other)
        return type(self)(*map(lambda x, y: x + y, self.args, other.args))

    def __sub__(self, other):
        self.len_test(other)
        return type(self)(*map(lambda x, y: x - y, self.args, other.args))

    def __mul__(self, other):
        self.len_test(other)
        return sum(map(lambda x, y: x * y, self.args, other.args))

    def norm(self):
        return sqrt(sum(map(lambda x: x ** 2, self.args)))

    def __eq__(self, other):
        self.len_test(other)
        return self.args == other.args


if __name__ == '__main__':

    coordinates = [(14, 51, 47), (39, 17, 64), (43, 20, 88), (42, 12, 66), (74, 81, 82), (27, 12, 48), (26, 73, 15),
                   (88, 46, 70), (45, 35, 20), (31, 100, 51), (36, 71, 28), (33, 51, 46), (60, 62, 76), (74, 92, 58),
                   (83, 74, 29), (96, 47, 60), (63, 62, 77), (76, 65, 46), (64, 33, 67), (79, 95, 30)]

    for x, y, z in coordinates:
        vector = Vector(x, y, z)
        print(vector + vector, vector - vector, vector * vector, vector.norm())
