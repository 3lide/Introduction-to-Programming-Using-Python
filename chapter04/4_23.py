x, y = eval(input("Enter a point with two coordinates: "))

xDistance = abs(x)
yDistance = abs(y)

if xDistance <= 5 and yDistance <= 2.5:
    print("Point ({:.1f}, {:.1f}) is in the rectangle".format(x, y))
else:
    print("Point ({:.1f}, {:.1f}) is not in the rectangle".format(x, y))