#(№ 3527) (А. Кабанов) Текстовый файл 24-153.txt содержит строку из заглавных букв A, B, C, D, E, F, всего не более чем
# из 106 символов. D-подстроками назовём последовательности идущих подряд символов D, ограниченные иными символами.
# Определите минимальную длину D-подстроки.
s = open('24-153.txt').readline().strip()
for i in 'QWERTYUIOPASFGHJKLZXCVBNM':
    s = s.replace(i, ' ')
s = s.split(' ')
q = [i for i in s if i !='']
print(q)
k_min = min(q, key=len)
print(len(k_min))
