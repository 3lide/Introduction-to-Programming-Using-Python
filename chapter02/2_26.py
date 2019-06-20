import turtle
import math

x, y = eval(input("Enter the coordinate of the center of a circle: "))
radius = eval(input("Enter the radius of the circle: "))

area = math.pi * radius * radius

turtle.setup(1000,1000)
t = turtle.Turtle()
t.pensize(5)
t.penup()
t.goto(x, y)
t.pendown()
t.write(str(format(area, ".2f")), align="center", 
font=("Times New Roman", 10, "bold"))
t.penup()
t.seth(-90)
t.forward(radius)
t.seth(0)
t.pendown()
t.circle(radius)
t.hideturtle()
turtle.done()
