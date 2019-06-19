number = eval(input("Enter a number between 0 and 1000: "))

firstDigit = number // 100
lastDigit = number % 10
secondDigit = (number // 10) % 10

sumOfDigits = firstDigit + secondDigit + lastDigit

print("The sum of the digits is",sumOfDigits)