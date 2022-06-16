from itertools import *
# степени
q = [
    [1000],
    [2, 500],
    [4, 250],
    [2, 2, 250],
    [4, 2, 125],
    [2, 4, 125],
    [2, 2, 2, 125],
    [4, 2, 5, 25],
    [2, 4, 5, 25],
    [4, 5, 2, 25],
    [5, 2, 4, 25],
    [5, 4, 2, 25],
    [2, 2, 2, 5, 25],
    [2, 2, 2, 5, 5, 5]
]
# комбинации простых чисел
w = []
for j in range(1, 7):
    for i in permutations([2, 3, 5, 7, 11, 13], j):
        w.append(i)
        print(i)
min_r = 1000000000000000000000
for i in w:
    p = 1
    r = len(i)
    for j in range(r):
        print(f'({i[j]}^{(q[r-1][j])})', end='*')
        p *= (i[j]**(q[r-1][j]))
    print(f'->P={p}')
    min_r = min(p, min_r)
print(min_r)