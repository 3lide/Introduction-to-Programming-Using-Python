import math
radius, length = eval(input('Enter the radius and length of cylinder: '))

area = radius * radius * math.pi
volume = area * length

print("The area is {:.4f}".format(area))
print("The volume is {:.1f}".format(volume))
