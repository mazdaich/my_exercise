from itertools import product

signs = '0123456789ABCDEF'

result = product(signs[:int(input())], repeat=int(input()))
for k in result:
    print(*k, sep='', end=' ')
