window = [['#FFFFFF' for _ in range(10_000)] for _ in range(10_000)]
with open('26-87.txt') as f:
    N = int(f.readline())
    for _ in range(N):
        s = f.readline().split()
        row, column = int(s[0]), int(s[1])
        window[row - 1][column - 1] = s[2].strip()
print(window[1])
count = 0
number_row = 0
max_count_pixel = 0
for i in range(10000):
    c = window[i].count('#00FF00')
    if c != 0:
        green = window[i].index('#00FF00')
        cur_count_pixel = 0
        while c != 1:
            if 9_997 > green > 2:
                if window[i][green - 3:green + 4].count('#0000FF') == 6:
                    print(i)
                    cur_count_pixel += 1
            green = window[i].index('#00FF00', green + 1)
            c -= 1
        count += cur_count_pixel
        if max_count_pixel <= cur_count_pixel:
            max_count_pixel = cur_count_pixel
            number_row = i + 1
print(count, number_row)