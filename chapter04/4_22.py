import math

x, y = eval(input("Enter a point with two coordinates: "))
distance = math.sqrt(x ** 2 + y ** 2)

if distance < 10:
    print("Point ({:.1f}, {:.1f}) is in the circle".format(x, y))
elif distance == 10:
    print("Point ({:.1f}, {:.1f}) is on the circle".format(x, y))
else:
    print("Point ({:.1f}, {:.1f}) is not in the circle".format(x, y))