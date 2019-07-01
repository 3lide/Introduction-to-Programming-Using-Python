x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points \
p0, p1 and p2: "))

status = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
if status == 0:
    if ((x2 >= x0 and x2 <= x1) or (x2 <= x0 and x1 >= x1)) and \
        ((y2 >= y0 and y2 <= y1) or (y2 >= y1 and y2 <= y0)):
        print("({:.1f}, {:.1f}) is on the line segment from ({:.1f}, {:.1f})".format(x2, y2, x0, y0), "to ({:.1f}, {:.1f})".format(x1, y1))
    else:
        print("({:.1f}, {:.1f}) is not on the line segment from ({:.1f}, {:.1f})".format(x2, y2, x0, y0), "to ({:.1f}, {:.1f})".format(x1, y1))
else:
    print("({:.1f}, {:.1f}) is not on the line segment from ({:.1f}, {:.1f})".format(x2, y2, x0, y0), "to ({:.1f}, {:.1f})".format(x1, y1))
