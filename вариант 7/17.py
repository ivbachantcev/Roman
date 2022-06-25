with open('17.txt') as f:
    min_19 = 10**7
    numbers = []
    for numb in f.readlines():
        c = int(numb)
        numbers.append(c)
        if c % 19 == 0 and c > 0:
            min_19 = min(min_19, c)
count = 0
max_abs = 0
for i in range(1, len(numbers)):
    c = numbers[i] + numbers[i - 1]
    if c < min_19:
        count += 1
        max_abs = max(max_abs, c)
print(count, max_abs)
