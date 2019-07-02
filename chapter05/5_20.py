for i0 in range(1, 7):
    for j0 in range(1, i0+1):
        print(j0, end = ' ')
    print()

for i1 in range(6, 0, -1):
    for j1 in range(1, i1+1):
        print(j1, end = ' ')
    print()

for i2 in range(1, 7):
    spaceNumber = 6 - i2
    for k in range(spaceNumber):
        print(' ', end = ' ')
    for j2 in range(i2, 0, -1):
        print(j2, end = ' ')
    print()

for i3 in range(6, 0, -1):
    spaceNumber = 6 - i3
    for t in range(spaceNumber):
        print(' ', end = ' ')
    for j3 in range(1, i3+1):
        print(j3, end = ' ')
    print()