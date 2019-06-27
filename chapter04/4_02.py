import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
number3 = random.randint(0, 9)

answer = eval(input("What is {}+{}+{} ? ".format(number1, number2, number3)))
print("{}+{}+{}={} is".format(number1, number2, \
    number3, answer), number1 + number2 + number3 == answer)
