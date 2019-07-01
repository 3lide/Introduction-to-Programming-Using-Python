import turtle

x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points \
p0, p1 and p2: "))

t1 = turtle.Turtle()

status = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
t1.penup()
t1.pensize(5)
t1.goto(x0, y0)
t1.write("p0({}, {})".format(x0, y0))
t1.pendown()
t1.goto(x1, y1)
t1.write("p1({}, {})".format(x1, y1))
t1.penup()
t1.goto(x2, y2)
t1.pendown()
t1.dot(5)

if status > 0:
    t1.write("p2 is on the left side of the line from p0 to p1")
elif status == 0:
    t1.write("p2 is on the same line from p0 to p1")
else:
    t1.write("p2 is on the right side of the line from p0 to p1")
turtle.done()
