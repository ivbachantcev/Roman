with open('24-174.txt') as f:
    count = 0
    max_len = 0
    for line in f:
        if line.count('R') < 30:
            k = len(line)
            position_liter = dict()
            for i in range(k):
                if line[i] in position_liter:
                    position_liter[line[i]].append(i)
                else:
                    position_liter[line[i]] = [i]
            for key, val in position_liter.items():
                cur_len = len(val)
                if cur_len > 1:
                    for i in range(cur_len - 1):
                        if val[i + 1] - val[i] > 1:
                            count += 1
                            max_len = max(max_len, val[i + 1] - val[i])
    print(count, max_len)