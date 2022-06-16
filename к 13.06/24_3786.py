with open('24-164.txt') as f:
    max_count = 0
    max_count_alpha = '0'
    dic_alpha = {i: 0 for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    for line in f:
        cur_count = 1
        cur_max = 1
        dic_alpha[line[0]] += 1
        for i in range(1, len(line.strip())):
            dic_alpha[line[i]] += 1
            if line[i - 1] == line[i]:
                cur_count += 1
                cur_max = max(cur_count, cur_max)
            else:
                cur_count = 1
        if cur_max > max_count:
            max_count = cur_max
            max_count_alpha, ma = '0', 0
            for letter in dic_alpha.keys():
                cc = line.count(letter)
                if cc > ma:
                    ma = cc
                    max_count_alpha = letter
print(max_count_alpha, dic_alpha[max_count_alpha])
