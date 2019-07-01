positiveCount = 0
negativeCount = 0
total = 0
while True:
    number = eval(input("Enter an integer, the input ends if it is 0: "))
    if number > 0:
        positiveCount += 1
    elif number == 0:
        break
    else:
        negativeCount += 1
    total += number

totalCount = positiveCount + negativeCount
if totalCount > 0:
    print("The number of positives is {}".format(positiveCount))
    print("The number of negatives is {}".format(negativeCount))
    print("The total is {}".format(total))
    print("The average is {:.2f}".format(total / (positiveCount + negativeCount)))
else:
    print("You didn't enter any numer")
