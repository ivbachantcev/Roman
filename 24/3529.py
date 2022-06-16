#Текстовый файл 24-153.txt содержит строку из заглавных букв A, B, C, D, E, F, всего не более чем из 106 символов.
# AF-подстроками назовём последовательности символов A, B, C, D, E, F, ограниченные в начале символом A, а в конце
# символом F (граничные символы входят в подстроку). Определите минимальную длину AF-подстроки.
# Подстроки, состоящие из двух символов, не учитывать.
s = open('24-153.txt').readline().strip()
posFirst = 0
posSecond = 0
k_min = 10**8
flag = False
for i in range(len(s)):
    if s[i] == 'A':
        posFirst = i
    if s[i] == 'F':
        posSecond = i
        flag = True
    if flag:
        if posFirst < posSecond and posSecond - posFirst > 1:
            k_min = min(k_min, len(s[posFirst:posSecond+1]))
        posFirst = 0
        posSecond = 0
        flag = False
print(k_min)
