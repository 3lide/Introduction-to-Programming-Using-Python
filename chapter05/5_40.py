import random

upCount = 0
downCount = 0
for i in range(1000000):
    number = random.randint(0, 1)
    if number == 0:
        upCount += 1
    else:
        downCount += 1
print("硬币向上的次数是{}，硬币向下的次数是{}".format(upCount, downCount))