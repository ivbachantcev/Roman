with open('26-s1.txt') as f:
    N = int(f.readline())
    products_more_100 = []
    salary = 0
    for line in f:
        q = int(line)
        if q <= 100:
            salary += q
        else:
            products_more_100.append(q)
products_more_100.sort()
salary += sum(products_more_100[:len(products_more_100) // 2]) * .9 + sum(products_more_100[len(products_more_100) // 2:])
print(round(salary), products_more_100[len(products_more_100) // 2 - 1])
print(len(products_more_100) // 2)