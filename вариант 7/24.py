with open('24.txt') as f:
    s = f.readline()
s = s.replace('NPO', '*')
s = s.replace('PNO', '*')
max_count = 0
count = 0
for i in range(len(s)):
    if s[i] == '*':
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print(max_count)