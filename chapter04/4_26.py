def isPalindrome(number):
    listNumber = list(str(number))
    reversedListNumber = listNumber[::-1]
    reversedStrNumber = "".join(reversedListNumber)
    reversedNumber = eval(reversedStrNumber)
    if reversedNumber == number:
        return True
    else:
        return False

def main():
    number = eval(input("Enter a three-digit integer: "))
    if isPalindrome(number):
        print("{} is a palindrome".format(number))
    else:
        print("{} is not a palindrome".format(number))

if __name__ == "__main__":
    main()