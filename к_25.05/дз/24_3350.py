
f = open('24-1.txt').readline()
pos_max = []
max_s = 0
for i in range(1, len(f) - 1):
    if f[i - 1] < f[i] > f[i + 1]:
        pos_max.append(i)
for i in range(len(pos_max) - 1):
    if pos_max[i + 1] - pos_max[i] > max_s:
        max_s = pos_max[i + 1] - pos_max[i]
print(max_s)