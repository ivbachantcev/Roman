with open('24-208.txt') as f:
    s = f.readline()
q = s.split('2022')
print(q)
max_len = 0
for i in range(1, len(q)-3):
    c = len(q[i - 1] + q[i] + q[i + 1] + q[i + 2] + q[i + 3]) + 16
    if c > max_len:
        max_len = c
print(max_len)
