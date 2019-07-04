import random

def isPointInArea1(point):
    if point[0] >= -1 and point[0] <= 0 and \
        point[1] >= -1 and point[1] <= 1:
        return True
    else:
        return False

def isPointInArea3(point):
    if point[0] + point[1] -1 <= 0 and point[0] >= 0 and \
        point[1] >= 0:
        return True
    else:
        return False

def main():
    count = 0
    for i in range(1000000):
        point = (2*random.random()-1, 2*random.random()-1)
        if isPointInArea1(point) or isPointInArea3(point):
            count += 1
    print("这个点落在奇数区域的概率是{:.4f}".format(count / 1000000))

if __name__ == "__main__":
    main()