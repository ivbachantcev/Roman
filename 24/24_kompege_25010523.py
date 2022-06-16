q = open('24.txt').readline()
k_max = 0
count = 0
for i in range(len(q)):
    if q[i] == 'B' and count % 2 == 0 or q[i] == 'A' and count % 2 == 1:
        count += 1
        k_max = max(k_max, count)
    else:
        if q[i] == 'B':
            count = 1
        else:
            count = 0
print(k_max)
count = 0
for i in range(len(q)):
    if q[i] == 'D' and count % 2 == 0 or q[i] == 'A' and count % 2 == 1:
        count += 1
        k_max = max(k_max, count)
    else:
        if q[i] == 'D':
            count = 1
        else:
            count = 0
count = 0
for i in range(len(q)):
    if q[i] == 'B' and count % 2 == 0 or q[i] == 'A' and count % 2 == 1:
        count += 1
        k_max = max(k_max, count)
    else:
        if q[i] == 'D':
            count = 1
        else:
            count = 0

