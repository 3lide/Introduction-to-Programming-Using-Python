def sumDigits(n):
    numberList = list(str(n))
    for i in range(len(numberList)):
        numberList[i] = eval(numberList[i])
    return sum(numberList)

print(sumDigits(235))