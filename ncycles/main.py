from itertools import tee, chain


def ncycles(obj, num):
    return chain.from_iterable(tee(obj, num))
