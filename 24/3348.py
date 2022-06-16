#(№ 3348) (Е. Джобс) Текстовый файл 24-j1.txt состоит не более чем из 106 кириллических символов К, О, Т.
# Определите максимальное количество подряд идущих комбинаций КОТ.
s = open('24-j1.txt').readline().strip()
k_max = 0
currCount = 0
for i in range(len(s)):
    if s[i] == 'К' and currCount % 3 == 0 or s[i] == 'О' and currCount % 3 == 1 or s[i] == 'Т' and currCount % 3 == 2:
        currCount += 1
    elif s[i] == 'К':
        currCount = 1
    else:
        currCount = 0
    if s[i] == 'Т':
        k_max = max(k_max, currCount)
print(k_max / 3)
