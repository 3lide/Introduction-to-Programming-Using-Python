import turtle

#绘制钟表
turtle.setup(1000,1000)

r1 = 300
r2 = r1 - 20
time = ['3', '12', '9', '6']

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.speed(9)
t2.speed(9)

#把第一个海龟移动至起点
t1.pensize(3)
t1.penup()
t1.goto(0, -r1)
t1.pendown()

#把第二个海龟移动至起点
t2.penup()
t2.goto(0, -r2)

for i in range(4):
    t1.circle(r1, 90)
    t2.circle(r2, 90)
    t2.write(time[i], align="left", font = ("Times New Roman", 15, "bold"))

t1.penup()
t1.home()
t1.pendown()
t1.pensize(10)
t1.goto(-100, 0)
t1.seth(180)
t1.turtlesize(3)
t1.stamp()
t1.home()
t1.pensize(5)
t1.goto(180, 0)
t1.turtlesize(2)
t1.stamp()
t1.home()
t1.pensize(3)
t1.goto(0, 260)
t1.turtlesize(1)
t1.seth(90)
t1.stamp()
t1.home()
t1.dot(15,'red')

t1.penup()
t1.goto(0, -(r1 + 30))
t1.seth(90)
t1.write("9:15:00", align="center", font=("Times New Roman", 20, "bold"))

t1.hideturtle()
t2.hideturtle()
turtle.done()
