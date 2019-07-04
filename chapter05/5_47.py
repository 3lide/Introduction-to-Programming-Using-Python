import turtle
import random

t1 = turtle.Turtle()
t1.penup()
t1.goto(-60, -50)
t1.seth(90)
t1.pendown()
t1.forward(100)
t1.right(90)
t1.forward(120)
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(120)
for i in range(10):
    x = random.randint(-60, 60)
    y = random.randint(-50, 50)
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.dot(3)
t1.hideturtle()
turtle.done()