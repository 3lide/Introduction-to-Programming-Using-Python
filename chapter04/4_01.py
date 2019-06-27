import math

a, b, c = eval(input("Enter a, b, c: "))

delta = b**2 - 4 * a * c

if delta > 0:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    print("The roots are {:.5f} and {:.5f}".format(r1, r2))
elif delta == 0:
    r = -b / (2 * a)
    print("The root is {:.5f}".format(r))
else:
    print("The equation has no real roots")