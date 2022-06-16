with open('24-209.txt') as f:
    s = f.readline()
s = s.replace('E', 'D')
s = s.replace('F', 'D')
q = s.split('D')
new_q = [i for i in q if i != '']
print(new_q)
max_count = 0
for line in new_q:
    cur_max = 1
    for i in range(len(line) - 1):
        if line[i] != line[i + 1]:
            cur_max += 1
            # поставил сюда, ибо может быть строчка, которая целиком правильная и лучше максимум пересчитывать постоянно
            max_count = max(max_count, cur_max - 1)
        else:
            cur_max = 1
print(max_count)