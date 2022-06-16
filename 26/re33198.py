# question 3
f = open('26.txt')
N, M = map(int, f.readline().split())
important_cargo = [] # грузы от 200 до 210 кг
another_cargo = [] # все остальные грузы
send_cargo = [] # грузы которые идут на отправку
weight = 0
for i in range(N):
    cargo = int(f.readline())
    if 200 <= cargo <= 210:
        important_cargo.append(cargo)
        weight += cargo
        send_cargo.append(cargo)
    else:
        another_cargo.append(cargo)
another_cargo.sort()
count_important = len(important_cargo) # кол-во грузов, которые 100% надо отвезти
# узнаём максимальное кол-во которое в принципе можем загрузить
for i in range(len(another_cargo)):
    if weight + another_cargo[i] <= M:
        send_cargo.append(another_cargo[i])
        weight += another_cargo[i]
print(sum(send_cargo), len(send_cargo))
for i in range(len(send_cargo) - 1, count_important, - 1):
    for j in range(len(another_cargo)):
        if weight - send_cargo[i] + another_cargo[j] <= M and send_cargo[i] < another_cargo[j]:
            weight = weight - send_cargo[i] + another_cargo[j]
            send_cargo[i] = another_cargo[j]

print(len(send_cargo), weight)