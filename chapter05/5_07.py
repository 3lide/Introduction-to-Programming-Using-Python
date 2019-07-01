import math

print("度\tSin\tCos")

for i in range(0, 361, 10):
    print("{}\t{:.4f}\t{:.4f}".format(i, math.sin(math.radians(i)), \
        math.cos(math.radians(i))))
