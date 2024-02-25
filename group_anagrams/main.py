from itertools import groupby


def group_anagrams(words):
    res = groupby(sorted(words, key=sorted), key=sorted)
    return [tuple(value) for key, value in res]


groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])

print(*groups)