def sum_div(n):
    div = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n // i)
    if div:
        return sum(div), max(div)
    return 0, 0


N = 520_000 + 1
count = 0
while count != 5:
    w = sum_div(N)
    if w[0] and int(str(w[0])[::-1]) == w[0]:
        print(N, w[1])
        count += 1
    N += 1
