#(№ 4988) (А. Кабанов) Назовём маской числа последовательность цифр, в
# которой также могут встречаться следующие символы:
#— символ «?» означает ровно одну произвольную цифру;
#— символ «*» означает любую последовательность цифр
# произвольной длины; в том числе «*» может задавать и пустую последовательность.
#Например, маске 123*4?5 соответствуют числа 123405 и 12300425. Среди натуральных чисел,
# не превышающих 109, найдите все числа, соответствующие маске 123*567? и делящиеся на 169 без остатка.
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце — соответствующие им частные от деления на 169.
w = 123
q = 0
while w < 10**9:
    r = '123' + (str(q) if q != 0 else '') + '5670'
    for i in range(10):
        w = int(r) + i
        if w % 169 == 0:
            print(w, w // 169)
    q += 1

