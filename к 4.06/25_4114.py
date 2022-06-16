def simple_numb(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


all_simple_numb = [i for i in range(3, 1_000_000 + 1) if simple_numb(i)]
for i in range(len(all_simple_numb) - 1):
    if all_simple_numb[i + 1] - all_simple_numb[i] - 1 >= 90:
        print(all_simple_numb[i], all_simple_numb[i + 1])
