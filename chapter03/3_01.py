import math 
length = eval(input("Enter the length from the center to a vertex: "))

s = 2 * length * math.sin(math.pi / 5)
area = 5 * s * s / (4 * math.tan(math.pi / 5))

print("The area of the pentagon is", format(area, ".2f"))