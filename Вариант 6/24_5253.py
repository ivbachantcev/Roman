with open('24-208.txt') as f:
    s = f.readline()
q = s.split('2022')
print(q)
max_len = 0
for i in range(len(q) - 4):
    c = len(q[i] + q[i + 1] + q[i + 2] + q[i + 3] + q[i + 4]) + 16 + 3
    if c > max_len:
        max_len = c
print(max_len)
