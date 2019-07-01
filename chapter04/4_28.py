x1, y1, width1, height1 = eval(input(
    "Enter r1's center x-, y-coordinates, width, and height: "
))
x2, y2, width2, height2 = eval(input(
    "Enter r2's center x-, y-coordinates, width, and height: "
))

#计算第一个矩形的左右边横坐标，上下边纵坐标
leftX1 = x1 - width1 / 2
rightX1 = x1 + width1 / 2
upperY1 = y1 + height1 / 2
lowerY1 = y1 - height1 / 2

#计算第二个矩形的左右边横坐标，上下边纵坐标
leftX2 = x2 - width2 / 2
rightX2 = x2 + width2 / 2
upperY2 = y2 + height2 / 2
lowerY2 = y2 - height2 / 2

#判断一个点是否在矩形中
def isPointInRectangle(point, rectangle):
    if point[0] >= rectangle[0] and point[0] <= rectangle[1] and \
        point[1] >= rectangle[2] and point[1] <= rectangle[3]:
        return True
    else:
        return False

rectangle1 = (leftX1, rightX1, lowerY1, upperY1)
rectangle2 = (leftX2, rightX2, lowerY2, upperY2)

#r1的四个顶点坐标
leftUpper1 = (leftX1, upperY1)
leftLower1 = (leftX1, lowerY1)
rightUpper1 = (rightX1, upperY1)
rightLower1 = (rightX1, lowerY1)

#r2的四个顶点坐标
leftUpper2 = (leftX2, upperY2)
leftLower2 = (leftX2, lowerY2)
rightUpper2 = (rightX2, upperY2)
rightLower2 = (rightX2, lowerY2)

#如果矩形r2在矩形r1中，那么r2的四个顶点坐标都应该在矩形r1中
if isPointInRectangle(leftUpper2, rectangle1) and \
    isPointInRectangle(leftLower2, rectangle1) and \
    isPointInRectangle(rightUpper2, rectangle1) and \
    isPointInRectangle(rightLower2, rectangle1):
    print("r2 is inside r1")
elif isPointInRectangle(leftLower1, rectangle2) and \
    isPointInRectangle(leftUpper1, rectangle2) and \
    isPointInRectangle(rightLower1, rectangle2) and \
    isPointInRectangle(rightUpper1, rectangle2):
    print("r1 is inside r2")

#如果矩形的某一个点在另一个矩形中，那么这两个矩形肯定相交
elif isPointInRectangle(leftUpper1, rectangle2) or \
    isPointInRectangle(leftLower1, rectangle2) or \
    isPointInRectangle(rightUpper1, rectangle2) or \
    isPointInRectangle(rightLower1, rectangle2) or \
    isPointInRectangle(leftUpper2, rectangle1) or \
    isPointInRectangle(leftLower2, rectangle1) or \
    isPointInRectangle(rightUpper2, rectangle1) or \
    isPointInRectangle(rightLower2, rectangle1):
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")