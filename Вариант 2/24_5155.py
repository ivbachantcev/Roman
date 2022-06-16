f = open('24-204.txt').readline()
cur_count = 0
max_count = 0
for i in range(0, len(f), 2):
    if f[i:i+2] in ('AA', 'CC'):
        cur_count += 1
        max_count = max(cur_count, max_count)
    else:
        cur_count = 0
print(max_count)
