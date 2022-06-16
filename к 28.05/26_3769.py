f = open('26-53.txt')
N = int(f.readline())
arr_numbers = []
arr_mid_sum = [0] * (10 ** 9)
for _ in range(N):
    numb = int(f.readline())
    arr_numbers.append(numb)
    arr_mid_sum[numb - 1] = 1
count = 0
max_middle_sum = 0
for i in range(N):
    if arr_numbers[i] % 2:
        for j in range(i + 1, N):
            if arr_numbers[j] % 2:
                cur_middle_sum = (arr_numbers[i] + arr_numbers[j]) // 2
                if arr_mid_sum[cur_middle_sum - 1]:
                    count += 1
                    max_middle_sum = max(max_middle_sum, cur_middle_sum)
print(count, max_middle_sum)