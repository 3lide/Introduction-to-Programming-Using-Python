import random

number1 = ord('A')
number2 = ord('Z')

number = random.randint(number1, number2)
print("随机产生一个大写字母为：{}".format(chr(number)))