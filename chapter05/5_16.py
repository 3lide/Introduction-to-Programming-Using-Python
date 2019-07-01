number1 = eval(input("Enter first integer: "))
number2 = eval(input("Enter second integer: "))

gcd = min(number1, number2)
while True:
    if number1 % gcd == 0 and number2 % gcd == 0:
        print("{}和{}的最大公因数是{}".format(number1, number2, gcd))
        break
    else:
        gcd -= 1