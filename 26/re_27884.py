q = open('27884.txt')
S, N = map(int, q.readline().split())
md = []
k = 0
k_max = 0
for i in range(N):
    s = int(q.readline())
    md.append(s)
if sum(md) <= S:
    k = N
    k_max = max(md)
else:
    d = []
    md.sort()
    sum_md = 0
    while sum_md + md[k] <= S:
        sum_md += md[k]
        d.append(md[k])
        k_max = max(k_max, md[k])
        k += 1
    for i in range(k, N):
        print(sum_md - d[-1] + md[i] <= S, md[k])
        if sum_md - d[-1] + md[i] <= S:
            sum_md = sum_md - d[-1] + md[i]
            d[-1] = md[i]
print(d)
print(S, sum_md, k, d[-1]) #k выводит правильно k_max выводит неправильно