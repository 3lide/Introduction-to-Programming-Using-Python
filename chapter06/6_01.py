def getPentagonalNumber(n):
    return int(n*(3*n-1)/2)

count = 0
for i in range(1, 101):
    print(format(getPentagonalNumber(i), ">10d"), end = ' ')
    count += 1
    if count == 10:
        print()
        count = 0
