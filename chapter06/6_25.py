def isPrimer(number):
    if number == 1:
        return False
    else:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                return False
        return True

def reverse(number):
    reversedNumber = int("".join(list(str(number))[::-1]))
    return reversedNumber

def isPalindrome(number):
    if str(number) == "".join(list(str(number))[::-1]):
        return True
    else:
        return False

def main():
    number = 1
    count = 0
    NUMBER_PER_LINE = 10
    while count < 1000:
        if isPrimer(number) and isPrimer(reverse(number)) and not \
            isPalindrome(number):
            print(format(number, ">5d"), end = " ")
            count += 1
            if count % 10 == 0:
                print()
        number += 1

if __name__ == "__main__":
    main()