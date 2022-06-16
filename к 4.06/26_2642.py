with open('26-k5.txt') as f:
    N, K, M = map(int, f.readline().split())
    price = [int(i) for i in f]
    price.sort()
    p1 = min(price[-M:])
    p2 = sum(price[:K]) // K
    print(p1, p2)
