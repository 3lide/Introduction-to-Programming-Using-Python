a, b, c, d, e, f = eval(input(
    "Enter a, b, c, d, e, f: "
))

delta = a * d - b * c

if delta == 0:
    print("The equation has no solution")
else:
    x = (e * d - b * f) / delta
    y = (a * f - e * c) / delta
    print("{:.1f} is and y is {:.1f}".format(x, y))