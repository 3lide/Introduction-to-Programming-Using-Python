number1 = eval(input("Enter number1: "))
number2 = eval(input("Enter number2: "))
number3 = eval(input("Enter number3: "))

if number1 > number2:
    number1, number2 = number2, number1
if number2 > number3:
    number2, number3 = number3, number2
if number1 > number2:
    number1, number2 = number2, number1

print("{}<{}<{}".format(number1, number2, number3))