import turtle

x, y = eval(input("Enter a point coordinates: "))

t1 = turtle.Turtle()
t1.pensize(5)
t1.penup()
t1.goto(-50, -25)
t1.pendown()
t1.seth(90)
t1.forward(50)
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(50)
t1.right(90)
t1.forward(100)

t1.penup()
t1.goto(x, y)
t1.pendown()
t1.dot(5,"red")

t1.penup()
t1.goto(0, -60)
t1.pendown()

if x >= -50 and x <= 50 and y >= -25 and y <= 25:
    t1.write("The point is inside the rectangle")
else:
    t1.write("The point is not inside the rectangle")

t1.hideturtle()
turtle.done()