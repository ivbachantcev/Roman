def simple_numb(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


def min_simple_div(n):
    div = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            if simple_numb(i):
                div.append(i)
            if i != n // i and simple_numb(n // i):
                div.append(n // i)
    return min(div)


count = 0
N = 20_222_022
while count != 5 and N > 2021:
    if not simple_numb(N):
        w = min_simple_div(N)
        if w > 100:
            print(N, w)
            count += 1
    N -= 1