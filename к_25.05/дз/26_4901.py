f = open('26-72.txt')
N, M, K = map(int, f.readline().split())
place = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    row, column = map(int, f.readline().split())
    place[row - 1][column - 1] = 1
count_position = 0
number_row = M + 1
max_position = 0
for i in range(M):
    cur_count_position = 0
    for j in range(N - 3):
        if sum(place[i][j:j+4]) == 0:
            cur_count_position += 1
    count_position += cur_count_position
    if cur_count_position > max_position:
        max_position = cur_count_position
        number_row = i
    elif cur_count_position == max_position:
        number_row = min(i, number_row)
print(count_position, number_row + 1)