import math

x1, y1, radius1 = eval(input("Enter circle1's center x-, y- coordinates, and radius: "))
x2, y2, radius2 = eval(input("Enter circle2's center x-, y- coordinates, and radius: "))

centroidDistance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if centroidDistance <= abs(radius1 - radius2):
    print("circle2 is inside circle1")
elif centroidDistance <= radius1 + radius2:
    print("circle2 overlaps circle1")
else:
    print("circle2 does not overlap circle1")