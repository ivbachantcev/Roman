# (№ 3440) (Е. Джобс) Для интервала [33333;55555] найти все простые числа, сумма цифр которых больше 35.
# Запишите найденные числа в порядке возрастания, справа от каждого – сумму его цифр.
def sumNumb(N):
    q = 0
    while N > 0:
        q += N % 10
        N //= 10
    return q

def simpleNumb(N):
    for i in range(2, round(N ** 0.5)):
        if N % i == 0:
            return False
    return True

for i in range(33333, 55555):
    if simpleNumb(i):
        q = sumNumb(i)
        if q > 35:
            print(i, q)