def reverse(number):
    numberList = list(str(number))[::-1]
    reversedNumber = int("".join(numberList))
    return reversedNumber

def isPalindrome(number):
    if number == reverse(number):
        return True
    else:
        return False

def main():
    number = eval(input("Enter an integer: "))
    if isPalindrome(number):
        print("{} is a palindrome".format(number))
    else:
        print("{} is not a palondrome".format(number))

if __name__ == "__main__":
    main()