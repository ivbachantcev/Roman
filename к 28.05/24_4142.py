f = open('24-171.txt')
rows = f.readlines()
max_len = 0
for row in rows:
    count = 0
    start = -1
    end = 0
    for i in range(len(row)):
        if row[i] == 'X' and count % 3 == 0 or row[i] == 'Y' and count % 3 == 1 or row[i] == 'Z' and count % 3 == 2:
            count += 1
            if start == -1:
                start = i
        else:
            if count % 3 == 0:
                if row[start - 1] in 'XYZ':
                    count += 1
                if row[i] in 'XYZ':
                    count += 1
                max_len = max(max_len, count)
            if row[i] == 'X':
                count = 1
            else:
                count = 0
            start = -1
print(max_len)