number = 1
numberList = []

while number != 0:
    number = eval(input("Enter a number (0: for end of input): "))
    numberList.append(number)

print("The largest number is", max(numberList))
print("The occurrence count of the largest number is", \
    numberList.count(max(numberList)))