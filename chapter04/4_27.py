#根据题目可以计算出三角形斜边的方程为：y = -1/2 * x + 100
#将坐标(x, y)代入-1/2 * x + 100 - y,若结果大于零，则该点在斜边下方，若结果小于零，
#则该点在斜边上方

x, y = eval(input("Enter a point's x- and y-coordinates: "))
number = -1/2 * x + 100 - y
if x > 0 and y > 0 and number > 0:
    print("The point is in the triangle")
else:
    print("The point is not in the triangle")