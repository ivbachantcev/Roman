# (№ 3932) Рассматриваются возрастающие последовательности из 5 идущих подряд чисел, больших 700000, такие, что
# количество делителей каждого следующего числа превосходит количество делителей предыдущего числа.
# Найдите такую последовательность, которая начинается с наименьшего возможного числа. Для каждого числа из этой
# последовательности запишите сначала само число, а затем количество его натуральных делителей.
def countDelit(N):
    deliteli = set()
    deliteli.add(1)
    deliteli.add(N)
    for q in range(2, round(N ** 0.5)):
        if N % q == 0:
            deliteli.add(q)
            deliteli.add(N // q)
    return len(deliteli)
for i in range(700000, 800000):
    q1 = countDelit(i)
    q2 = countDelit(i+1)
    q3 = countDelit(i+2)
    q4 = countDelit(i+3)
    q5 = countDelit(i+4)
    if q1 < q2 < q3 < q4 < q5:
        print(i, q1)
        print(i+1, q2)
        print(i+2, q3)
        print(i+3, q4)
        print(i+4, q5)
        break
