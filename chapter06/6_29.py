def isValid(number):
    if getSize(number) >= 13 and getSize(number) <= 16:
        if prefixMatched(number, 4) or prefixMatched(number ,5) or \
            prefixMatched(number, 6) or getPrefix(number, 2) == 37:
            return True if (sumOfDoubleEvenPlace(number) + 
            sumOfOddPlace(number)) % 10 == 0 else False

def sumOfDoubleEvenPlace(number):
    numberList = []
    oddPlaceNumberList = []
    for i in range(len(list(str(number)))):
        numberList.append(int(list(str(number))[i]))
    numberList.reverse()
    for j in range(1, len(numberList), 2):
        oddPlaceNumberList.append(numberList[j])
    doubleOddPlaceNumber = [i*2 for i in oddPlaceNumberList]
    digitOddPlaceNumber = [getDigit(i) for i in doubleOddPlaceNumber]
    return sum(digitOddPlaceNumber)

def getDigit(number):
    numberList = []
    for i in range(len(list(str(number)))):
        numberList.append(int(list(str(number))[i]))
    return sum(numberList)

def sumOfOddPlace(number):
    numberList = []
    totalNumber = 0
    for i in range(len(list(str(number)))):
        numberList.append(int(list(str(number))[i]))
    numberList.reverse()
    for j in range(0, len(numberList), 2):
        totalNumber += numberList[j]
    return totalNumber

def prefixMatched(number, d):
    return True if int(str(number)[0]) == d else False

def getSize(number):
    return len(str(number))

def getPrefix(number, k):
    if len(str(number)) <= k:
        return number
    else:
        return int(str(number)[0:k])

def main():
    number = eval(input("请输入信用卡号："))
    print("您的信用卡是合法的") if isValid(number) else print("您的信用卡不合法")

if __name__ == "__main__":
    main()