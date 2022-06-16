s = open('24-197.txt').readline()
s = s.replace('ZXX', '*')
s = s.replace('ZYY', '*')
s = s.replace('X', 'Y')
s = s.replace('ZYY', '+')
cur_count = 0
max_count = 0
for i in range(len(s)):
    if s[i] == '+':
        cur_count += 1
        
    else:
        max_count = max(max_count, cur_count)
        cur_count = 0
print(max_count)

