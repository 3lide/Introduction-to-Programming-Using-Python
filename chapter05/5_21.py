lineNumber = eval(input("Enter the number of line: "))

for line in range(1, lineNumber + 1):
    spaceNumber = lineNumber - line
    for i in range(spaceNumber):
        print(format("", ">3s"), end = ' ')
    for j in range(1, line+1):
        print(format(2**(j-1), "3d"), end = ' ')
    if line == 1:
        for k in range(spaceNumber):
            print(format("", ">3s"), end = ' ')
    else:
        for t in range(line-1, 0, -1):
            print(format(2**(t-1), "3d"), end = ' ')
        for l in range(spaceNumber):
            print(format("", ">3s"), end = ' ')
    print()