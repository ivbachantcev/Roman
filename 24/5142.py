f = open('24-200.txt').readlines()
print(f)
#195.?2.1*5.14
count = 0
for i in range(10):
    for j in range(10):
        t = '195.'+str(i)+'2.1'+str(j)+'5.14'+'\n'
        if t in f:
            count += f.count(t)
    t = '195.'+str(i)+'2.1'+'5.14'+'\n'
    if t in f:
        count += f.count(t)

print(count)