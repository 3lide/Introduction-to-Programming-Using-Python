import random

#产生两个小于100的整数
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

answer = number1 * number2

print("{} * {} = {}".format(number1, number2, answer))