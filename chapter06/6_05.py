def displaySortedNumbres(num1, num2, num3):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1
    return [num1, num2, num3]

def main():
    num1, num2, num3 = eval(input("Enter three numbers: "))
    sortedNumbers = displaySortedNumbres(num1, num2, num3)
    print("The sorted numbers are", sortedNumbers[0], 
    sortedNumbers[1], sortedNumbers[2])

if __name__ == "__main__":
    main()