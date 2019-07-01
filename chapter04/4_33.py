number = eval(input("Enter a decimal value (0 to 15): "))

if number <= 15 and number >= 0:
    hexValue = hex(number)
    hexValue = str(hexValue)[-1].upper()
    print("The hex value is", hexValue)
else:
    print("Invalid input")
