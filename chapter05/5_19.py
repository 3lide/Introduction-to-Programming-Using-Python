number = eval(input("Enter the number of line: "))

for line in range(1, number+1):
    spaceNumber = number - line
    for i in range(spaceNumber):
        print("".center(2), end = ' ')
    for j in range(line, 0, -1):
        print(str(j).center(2),  end = ' ')
    if line == 1:
        for k in range(spaceNumber):
            print("".center(2), end = ' ')
    else:
        for t in range(2, line+1):
            print(str(t).center(2), end = ' ')
        for l in range(spaceNumber):
            print("".center(2), end = ' ')
    print()