def check_div(n):
    return str(n).count('7') > 3



def s(n):
    div = []
    for i in range(2, round(n**.5) + 1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n // i)
    if len(div) < 3:
        return 0
    div.sort()
    return div[-1] + div[-2] + div[-3]


N = 10_000_000 + 1
count = 0
while count != 5:
    w = s(N)
    if w and check_div(w):
        print(w)
        count += 1
    N += 1
    