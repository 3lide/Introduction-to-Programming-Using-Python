import turtle

def drawHexagon(startPoint, sideLength):
    x = startPoint[0]
    y = startPoint[1]
    t = turtle.Turtle()
    t.pensize(5)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(30)
    for i in range(6):
        t.forward(sideLength)
        t.left(60)
    
    t.hideturtle()

def main():
    sideLength = eval(input("Enter the side length of hexagon: "))
    turtle.setup(1000, 1000)
    point1 = (-sideLength, 0)
    drawHexagon(point1, sideLength)
    point2 = (-sideLength, -2 * sideLength)
    drawHexagon(point2, sideLength)
    point3 = (sideLength, 0)
    drawHexagon(point3, sideLength)
    point4 = (sideLength, -2 * sideLength)
    drawHexagon(point4, sideLength)
    turtle.done()

if __name__ == "__main__":
    main()
