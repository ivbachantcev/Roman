for k in range(1, 1000000):
    M = 950_000_000 + k
    count_2 = 0
    while M % 2 == 0:
        count_2 += 1
        M //= 2
    if count_2 % 2 == 0:
        continue
    f = 0
    while M != 1:
        count = 0
        count_d = 0
        for i in range(3, round(M**.5)+1):
            if M % i == 0:
                count_d = 1
                while M % i == 0:
                    count += 1
                    M //= i
                break
        if count % 2 == 1:
            f = 1
            break
        if count_d == 0:
            f = 1
            break
    if f == 0:
        print(k)