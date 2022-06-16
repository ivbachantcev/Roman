f = open('26-78.txt')
N, start, end = map(int, f.readline().split())
watcher = [list(map(int, f.readline().split())) for _ in range(N)]
watcher.sort()
print(start, end)
prom_end = start
t = -1
count = 0
for i in range(N):
    left = watcher[i][0]
    right = watcher[i][1]
    if left <= prom_end:
        t = max(t, right)
    else:
        prom_end = t
        t = max(prom_end, right)
        count += 1
    if t >= end:
        count += 1
        break
print(count)