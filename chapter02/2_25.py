import turtle

x, y = eval(input("Enter the coordinate of the center of a rectangle:"))
width = eval(input("Enter the width of the rectangle: "))
height = eval(input("Enter the height of the rectangle: "))

turtle.setup(1000, 1000)
t = turtle.Turtle()
t.pensize(5)
t.penup()
startPointX = x + width / 2
startPointY = y + height / 2
t.goto(startPointX, startPointY)
t.pendown()
t.seth(180)
t.forward(width)
t.left(90)
t.forward(height)
t.left(90)
t.forward(width)
t.left(90)
t.forward(height)
t.hideturtle()

turtle.done()