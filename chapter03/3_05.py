import math

numberOfSide = eval(input("Enter the number of side: "))
sideLength = eval(input("Enter the side: "))

area = numberOfSide * sideLength ** 2 / (4 * math.tan(math.pi / numberOfSide))

print("The area of the polygon is", format(area, ".2f"))