#(№ 2715) (Е. Джобс) Текстовый файл 24-j7.txt состоит не более чем из 106 десятичных цифр.
# Найдите максимальную длину последовательности, которая состоит из цифр одинаковой четности.
# Например, в последовательности 1533244622185452354, 5 последовательностей с нечетными цифрами: 1533, 1, 5, 5, 35;
# и 5 с четными: 244622, 8, 4, 2, 4. Следовательно, искомая последовательность – 244622.
# В качестве ответа укажите максимальную длину найденной последовательности.
s = open('24-j7.txt').readline().strip()
k_max1 = 0
k_max2 = 0
s1 = ''
s2 = ''
for i in range(len(s)):
    if int(s[i]) % 2:
        s1 += s[i]
    else:
        k_max1 = max(len(s1), k_max1)
        s1 = ''
    if int(s[i]) % 2 == 0:
        s2 += s[i]
    else:
        k_max2 = max(len(s2), k_max2)
        s2 = ''
print(max(k_max1, k_max2))