hexCharacter = input("ENter a hex character: ")
hexCharacter = "0x" + hexCharacter

try:
    decimalValue = int(hexCharacter, 16)
except ValueError:
    print("Invalid input")
else:
    print("The decimal value is", decimalValue)