with open('24-180.txt') as f:
    s = f.readline()
max_count = 0
arr_step = [0, 0, 0, 0]
for i in range(len(s) - 3):
    if int(s[i: i + 4]) <= 2359:
        arr_step[i % 4] += 1
        max_count = max(max_count, arr_step[i % 4])
    else:
        arr_step[i % 4] = 0
print(max_count)
