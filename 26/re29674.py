# question_2
f = open('inf_22_10_20_26.txt')
N = int(f.readline())
products_sale = []
products_not_sale = []
for i in range(N):
    product = int(f.readline())
    if product > 50:
        products_sale.append(product)
    else:
        products_not_sale.append(product)
allPrice = sum(products_not_sale)
products_sale.sort()
max_product_sale = 0
for i in range(len(products_sale)):
    if i < len(products_sale) // 2:
        allPrice += products_sale[i] * 0.75
        max_product_sale = products_sale[i]
    else:
        allPrice += products_sale[i]
print(round(allPrice), max_product_sale)
