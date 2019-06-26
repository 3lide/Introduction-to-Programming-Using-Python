number = eval(input("Enter an integer: "))

string = str(number)
lengthOfNumber = len(string)

reverseString = []
for i in range(-1, -lengthOfNumber-1, -1):
    reverseString.append(string[i])

reverseNumber = "".join(reverseString)
print(reverseNumber)