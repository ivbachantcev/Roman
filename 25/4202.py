# (№ 4202) (Б. Баобаба) Числа-близнецы — это такие простые числа, которые отличаются друг от друга на 2.
# Найдите все пары чисел-близнецов в диапазоне [3 000 000; 10 000 000].
# В ответе запишите количество найденных пар и среднее арифметическое последней пары.
def simpleNumb(N):
    w = 2
    while w**2 <= N:
        if N % w == 0:
            return False
        w += 1
    return True

countP = 0
p1 = 0
p2 = 0
for i in range(3000003, 10000000, 2):
    delit = 2
    w = 2
    if (i % 2) * ((i - 2) % 2) != 0:
        #print(i, i -2)
        if simpleNumb(i) and simpleNumb(i - 2):
            countP += 1
            p1 = i
            p2 = i - 2
print(countP, (p1 + p2) / 2)
