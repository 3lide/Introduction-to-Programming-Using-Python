def reverse(number):
    numberList = list(str(number))[::-1]
    reversedNumber = int("".join(numberList))
    return reversedNumber

def main():
    number = eval(input("Enter an integer: "))
    print("{}的反向数是{}".format(number, reverse(number)))

if __name__ == "__main__":
    main()