with open('26.txt') as f:
    N = int(f.readline())
    products = []
    for i in range(N):
        products.append(int(f.readline()))
products.sort()
user_price = sum(products[::-1][: N // 4]) / 2 + sum(products[::-1][N // 4:])
shop_price = sum(products[: N // 4]) / 2 + sum(products[N // 4:])
print(user_price, shop_price)