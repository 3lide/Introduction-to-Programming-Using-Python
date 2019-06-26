# -*- coding: utf-8 -*-

import math

sideLength = eval(input("Enter the side: "))
area = 5 * sideLength * sideLength / ( 4 * math.tan(math.pi / 5))

print("The area of the pentagon is", format(area, ".2f"))