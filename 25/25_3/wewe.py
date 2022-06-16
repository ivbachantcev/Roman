from itertools import *


def all_division(n):
    b = []
    for e in range(2, n + 1):
        if n % e == 0:
            b.append(e)
    return b


A = all_division(1000)
# словарь из n списков в которых комбинации из n степеней
powers = {
    1: [], 2: [], 3: [], 4: [], 5: [], 6: [],
}
for j in range(1, 6 + 1):
    flag = True
    if j == 6:
        for i in product([2, 5], repeat=j):
            p = 1
            for k in i:
                p *= k
            if p == 1000:
                powers[j].append(i)
    else:
        for i in product(A, repeat=j):
            p = 1
            for k in i:
                p *= k
            if p == 1000:
                powers[j].append(i)
# словарь из n списков в которых находятся комбинации из n простых чисел
simpleNumbers = {
    1: [], 2: [], 3: [], 4: [], 5: [], 6: [],
}
for j in range(1, 7):
    for i in permutations([2, 3, 5, 7, 11, 13], j):
        simpleNumbers[j].append(i)
min_r = 1000000000000000000000
maxDiv = 0
for i in range(1, 7):
    z = simpleNumbers[i]
    r = powers[i]
    for number in z:  # numbers - последовательность из прост чисел
        for power in powers[i]:  # powers - последовательности из степеней
            p = 1  # print(f'({number[count]}^{(power[count] - 1)})', end='*')
            for count in range(i):
                p *= (number[count] ** (power[count] - 1))
            if min_r > p:
                min_r = p
                maxDiv = max(number)
print(min_r, maxDiv)
