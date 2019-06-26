import turtle

sideLength = eval(input("Enter the side length: "))

#绘制五角星
turtle.setup(1000, 1000)
turtle.pensize(5)
turtle.penup()
turtle.goto(0, sideLength / 2)
turtle.setheading(-72)
turtle.pendown()
turtle.forward(sideLength)
turtle.right(144)
turtle.forward(sideLength)
turtle.right(144)
turtle.forward(sideLength)
turtle.right(144)
turtle.forward(sideLength)
turtle.right(144)
turtle.forward(sideLength)
turtle.turtlesize(3)
turtle.hideturtle()
turtle.done()