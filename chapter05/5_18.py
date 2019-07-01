#计算number的最大素数因子
def getMaxPrimeFactor(number):
    maxPrimerFactor = int(number / 2)
    while maxPrimerFactor >= 2:
        if isPrimer(maxPrimerFactor):
            if number % maxPrimerFactor == 0:
                break
            else:
                maxPrimerFactor -= 1
        else:
            maxPrimerFactor -= 1
    return maxPrimerFactor

def isPrimer(number):
    if number == 2 and number == 3:
        return True
    else:
        count = int(number / 2)
        for i in range(2, count + 1):
            if number % i == 0:
                return False
        return True

def main():
    number = eval(input("Enter an integer: "))
    while True:
        if isPrimer(number):
            print(number)
            break
        else:
            primerFactor = getMaxPrimeFactor(number)
            print(primerFactor, end = ' ')
            number = number // primerFactor

if __name__ == "__main__":
    main()