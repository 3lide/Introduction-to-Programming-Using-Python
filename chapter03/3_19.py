import turtle

x1, y1 = eval(input("Enter the first point's coordinate: "))
x2, y2 = eval(input("Enter the second point's coordinate: "))

turtle.setup(900, 900)
t1 = turtle.Turtle()
t1.penup()
t1.pensize(5)
t1.goto(x1, y1)
t1.write("({},{})".format(x1, y1))
t1.pendown()
t1.goto(x2, y2)
t1.write("({},{})".format(x2, y2))
t1.hideturtle()

turtle.done()