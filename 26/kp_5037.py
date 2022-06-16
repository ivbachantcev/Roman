f = open('26-79.txt')
N, K = map(int, f.readline().split())
forest = {}
for i in range(N):
    line, position = map(int, f.readline().split())
    if line in forest:
        forest[line].append(position)
    else:
        forest[line] = [position]
max_line = 0
min_position = 10**6
for line in forest:
    if len(forest[line]) != 1:
        forest[line].sort()
        m = 10**6
        for i in range(len(forest[line]) - 1):
            if forest[line][i + 1] - forest[line][i] - 1 == K:
                m = forest[line][i] + 1
                break
        if m != 10**6 and line > max_line:
            max_line = line
            min_position = m
print(max_line, min_position)