with open('26-52.txt') as f:
    N = int(f.readline())
    numbers = [int(line) for line in f]
count = 0
min_middle_sum = 10**10
numbers.sort()
for i in range(N - 1):
    for j in range(i + 1, i + 100 + 2):
        if j < N:
            if (numbers[i] + numbers[j]) % 10 == 0:
                count += 1
                min_middle_sum = min(min_middle_sum, (numbers[i] + numbers[j]) // 2)
print(count, min_middle_sum)