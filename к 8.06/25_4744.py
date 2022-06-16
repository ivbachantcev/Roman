def s(n):
    div = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n // i)
    if len(div) < 2:
        return 0
    else:
        div.sort()
        return div[-1] + div[-2]


count = 0
N = 10_000_000 + 1
while count != 5:
    w = s(N)
    if 0 < w < 100_000 and w % 1000 == 112:
        print(w)
        count += 1
    N += 1