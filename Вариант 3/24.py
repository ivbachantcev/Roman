f = open('24-191.txt').readline().strip()
q = f.split('A')[1:-1]
count = 0
for i in q:
    if len(i) <= 10 and 'B' not in i:
        count += 1
print(count)