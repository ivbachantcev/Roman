# Рассматриваются целые числа, принадлежащих числовому отрезку [523456; 578925], которые представляют собой
# произведение двух различных простых делителей. Найдите такое из этих чисел, у которого два простых
# делителя меньше всего отличаются друг от друга. В ответе запишите простые делители этого числа в
# порядке возрастания. Если подходящих чисел несколько, запишите в ответе делители наименьшего из них.
def simple_div(n):
    for i in range(2,round(n**.5)+1):
        if n % i == 0:
            return False
    return True


def count_div(n):
    d = []
    count = 0
    for i in range(2, round(n**.5)+1):
        if n % i == 0:
            if simple_div(i):
                d.append(i)
            else:
                break
            if n // i != i and simple_div(n // i):
                d.append(n // i)
            else:
                break
    if len(d) == 2:
        return d
    else:
        return []
min_k = 10**9
min_d = []
for i in range(523456, 578925 + 1):
    w = count_div(i)
    if w != [] and abs(w[0]-w[1]) < min_k:
        min_d = w
        min_k = abs(w[0]-w[1])

print(sorted(min_d))


