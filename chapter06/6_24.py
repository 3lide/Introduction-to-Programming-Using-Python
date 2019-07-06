def isPrimer(number):
    if number == 1:
        return False
    else:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                return False
        return True

def isPalindrome(number):
    numberList = list(str(number))
    if str(number) == "".join(numberList[::-1]):
        return True
    else:
        return False

def main():
    count = 0
    NUMBER_PER_LINE = 10
    number = 1
    while count < 200:
        if isPalindrome(number) and isPrimer(number):
            print(format(number, ">7d"), end = " ")
            count += 1
            if count % 10 == 0:
                print()
        number += 1

if __name__ == "__main__":
    main()