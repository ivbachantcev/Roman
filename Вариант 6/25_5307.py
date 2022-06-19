def simple_numb(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


def sort_div(arr1, arr2, n):
    if simple_numb(n):
        arr1.append(n)
    if n % 2 == 0:
        arr2.append(n)


def M(n):
    E = []
    P = []
    if n % 2 == 0:
        E.append(n)
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            sort_div(P, E, i)
            if i != n // i:
                sort_div(P, E, n // i)
    a, b = len(E), len(P)
    if a == b and a * b != 0:
        return abs(sum(E) - sum(P))
    return 0


count = 0
start = 100_000_000 + 1
while count != 5:
    w = M(start)
    if w != 0:
        print(start, w)
        count += 1
    start += 1