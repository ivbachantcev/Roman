def sum_digit(n):
    result = 0
    while n != 0:
        result += n % 10
        n //= 10
    return result == 17


def d(n):
    div = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            if sum_digit(i):
                div.append(i)
            if i != n // i and sum_digit(n // i):
                div.append(n // i)
    return div


N = 300_000_000 - 1
count = 0
while count != 5:
    w = d(N)
    if len(w) > 4:
        w.sort()
        print(w[-5], len(w))
        count += 1
    N -= 1