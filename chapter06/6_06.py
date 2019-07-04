def displayPattern(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(format("", ">3s"), end = ' ')
        for k in range(i, 0, -1):
            print(format(k, ">3d"), end = " ")
        print()

displayPattern(20)