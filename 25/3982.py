#(№ 3982) Найдите все натуральные числа, N, принадлежащие отрезку [100 000 000; 300 000 000], которые можно представить
# в виде N = 2^m•7^n, где m – нечётное число, n – чётное число. В ответе запишите все найденные числа
# в порядке возрастания, а справа от каждого числа – сумму m+n.
m = 0
n = 0
for i in range(100000000, 300000001):
    q = i
    while q % 2 == 0:
        m += 1
        q //= 2
    while q % 7 == 0:
        n += 1
        q //= 7
    if q == 1 and m % 2 == 1 and n % 2 == 0:
        print(i, m + n)
    m, n = 0, 0