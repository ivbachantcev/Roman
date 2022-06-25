def check(arr, numb):
    if numb % 161 == 0:
        arr.append((numb, numb // 161))


numbers = []
for i in range(10):
    # * пустота
    c = int('124' + str(i) + '65')
    check(numbers, c)
    for j in range(100):
        # * два символа
        c = int('12' + str(j % 10) + str(j // 10) + '4' + str(i) + '65')
        check(numbers, c)
    # * один символ
    for j in range(10):
        c = int('12' + str(j) + '4' + str(i) + '65')
        check(numbers, c)
for w in sorted(numbers):
    print(w[0], w[1])