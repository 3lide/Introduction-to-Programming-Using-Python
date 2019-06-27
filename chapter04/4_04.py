import random

number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

answer = eval(input("Enter the answer of {}+{} ".format(number1, number2)))
print("{}+{}={} is".format(number1, number2, answer), \
    number1 + number2 == answer)