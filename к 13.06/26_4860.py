with open('26-70.txt') as f:
    g = [int(f.readline()) for _ in range(int(f.readline()))]
g.sort()
global_sum = 0
count = 0
for x in g:
    if x - global_sum > 1:
        print(global_sum + 1, count)
        break
    count += 1
    global_sum += x
else:
    print(global_sum + 1, count)