print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (not (not x or z) or y or not w) == False:
                    print(x, y, z, w, 0)
