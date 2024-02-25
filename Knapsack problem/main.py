from collections import namedtuple
from itertools import combinations


ves = int(input())

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

min_ves = min(items, key=lambda x: x.mass).mass

if ves < min_ves:
    print('Рюкзак собрать не удастся')
else:
    res = []
    for i in range(1, 11):
        for j in set(combinations(items, i)):
            if sum([x.mass for x in j]) <= ves:
                res.append(j)
    count = 0

    for i in res:
        price = sum([x.price for x in i])
        if price > count:
            count = price
            x = i

    for i in sorted(x):
        print(i.name)
