def dlinna(file_name):
    left = 0
    right = 0
    f = open(file_name)
    N, K = int(f.readline().split())
    d = 10**9
    all_chisla = set([i + 1 for i in range(K)])
    while right < N:
