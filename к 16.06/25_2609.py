def simple_numb(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


def check_div(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            if simple_numb(i):
                if i != n // i and simple_numb(n // i):
                    if i % 10 == (n // i) % 10:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    return False


count = 0
sum_number = 0
for N in range(264871, 322989):
    if check_div(N):
        count += 1
        sum_number += N
print(count, sum_number // count)