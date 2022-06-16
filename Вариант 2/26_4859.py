f = open('26-69.txt')
N = int(f.readline())
places = dict()
for _ in range(N):
    row, column = map(int, f.readline().split())
    if row in places:
        places[row].append(column)
    else:
        places[row] = [column]
max_row = 0
max_places = 0
for key in places:
    places[key].sort()
    cur_count = 1
    max_cur_count = 0
    for i in range(len(places[key]) - 1):
        if places[key][i + 1] - places[key][i] == 1:
            cur_count += 1
        else:
            max_cur_count = max(max_cur_count, cur_count)
            cur_count = 1
    if max_cur_count > max_places:
        max_places = max_cur_count
        max_row = key
    elif max_cur_count == max_places:
        max_row = max(max_row, key)
print(max_row, max_places)
