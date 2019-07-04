import turtle

t1 = turtle.Turtle()
x = 0
y = -50
radius = 50

for i in range(10):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.circle(radius)
    y -= 10
    radius += 10

turtle.done()