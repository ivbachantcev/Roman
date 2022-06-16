#question_1
f = open('26_demo.txt')
S, N = map(int, f.readline().split())
users = [int(i) for i in f.readlines()]
f.close()
users.sort()
count_users = 0
saved_users = []
c = 0
for i in range(len(users)):
    if c + users[i] <= S:
        c += users[i]
        saved_users.append(users[i])
max_user = saved_users[-1]
for i in range(len(saved_users), len(users)):
    if c - max_user + users[i] <= S:
        c = c - max_user + users[i]
        max_user = users[i]
print(len(saved_users), max_user)
