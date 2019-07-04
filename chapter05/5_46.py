import math

print("Enter ten numbers: ")
number = []
for i in range(10):
    number.append(eval(input()))

mean = sum(number) / 10

newNumber = []
for j in range(len(number)):
    newNumber.append(number[j]**2)

deviation = math.sqrt((sum(newNumber) - sum(number)) / (10 -1))

print("The mean is", mean)
print("The standard deviation is", deviation)