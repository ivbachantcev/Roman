# (№ 4986) (М. Фирсов) Простой палиндром – это число, которое читается одинаково слева направо и справа налево,
# и при этом является простым, то есть не имеет делителей, кроме 1 и самого себя.
# Примеры простых палиндромов – 101, 131, 151 и т.д.
# Все простые палиндромы на отрезке [100; 1 000 000 000] распределили по группам с одинаковыми произведениями цифр
# (если в числе есть цифра 0, она не учитывается в произведении: для числа 16061 произведением цифр будет 36).
# Найдите 5 самых больших по значению чисел в группе с наибольшим количеством элементов.
# Расположите эти числа в порядке возрастания.
def simpleNumb(N):
    for i in range(2, round(N**0.5)):
        if N % i == 0:
            return False
    return True

def mulDigit(N):
    w = 1
    while N != 0:
        if N % 10 != 0:
            w *= N % 10
        N //= 10
    return w

w = dict()
q = 0
while q < 10**5:
    ch_p = 0
    nch_p = 0
    for i in range(10):
        f = str(q)
        s = str(i)
        if q < 10**4:
            nch_p = int(f + s + f[::-1])
            if simpleNumb(nch_p):
                r = mulDigit(nch_p)
                if r in w:
                    w[r].append(nch_p)
                else:
                    w[r] = [nch_p]
        if q < 10**5:
            ch_p = int(f + s*2 + f[::-1])
            if simpleNumb(ch_p):
                r = mulDigit(ch_p)
                if r in w:
                    w[r].append(ch_p)
                else:
                    w[r] = [ch_p]

    q += 1
t = []
tt = 0
for key, val in w.items():
    s = len(w[key])
    if s > tt:
        t = w[key]
        tt = s
sorted(t)
print(t[-5], t[-4], t[-3], t[-2], t[-1], sep='\n')
