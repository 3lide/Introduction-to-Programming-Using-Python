import math

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points \
for a triangle: "))

A = (x1, y1)
B = (x2, y2)
C = (x3, y3)

def main():
    side1 = getDistance(A, B)
    side2 = getDistance(B, C)
    side3 = getDistance(A, C)
    
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    print("The area of the triangle is", format(area, ".1f"))

#计算两点之间的距离
def getDistance(point1, point2):
    distance = math.sqrt((point1[0] - point2[0]) ** 2 + \
        (point1[1] - point2[1]) ** 2)
    return distance

if __name__ == "__main__":
    main()