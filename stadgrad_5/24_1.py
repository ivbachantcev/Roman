s = 'A' + open('24.txt').readline() + 'A'
position = [i for i in range(len(s)) if s[i] in 'AB']
max_len = 0
for i in range(len(position)-4):
    max_len = max(max_len, position[i+4] - position[i] - 1)
print(max_len)