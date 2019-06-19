import turtle

#绘制三角形
turtle.setup(1000, 1000)
turtle.penup()
turtle.goto(-300, -300)
turtle.pendown()
turtle.pensize(5)
turtle.setheading(60)
turtle.forward(600)
turtle.setheading(-60)
turtle.forward(600)
turtle.setheading(180)
turtle.forward(600)
turtle.done()