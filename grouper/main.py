from itertools import tee, zip_longest


def grouper(obj, num):
    w = tee(obj, num)
    for i in range(1, len(w)):
        for j in range(i):
            next(w[i], None)
    res = []
    w = list(zip_longest(*w))
    for i in range(0, len(w), num):
        res.append(w[i])
    return res
