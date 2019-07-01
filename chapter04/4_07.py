amount = eval(input("Enter an amount, for example, 11.56: "))

remainingAmount =int(amount * 100)

numberOfDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfPennies = remainingAmount

print("Your amount {} consists of".format(amount))
if numberOfDollars > 0:
    if numberOfDollars > 1:
        print("\t{} dollars".format(numberOfDollars))
    else:
        print("\t{} dollar".format(numberOfDollars))

if numberOfQuarters > 0:
    if numberOfQuarters > 1:
        print("\t{} quarters".format(numberOfQuarters))
    else:
        print("\t{} quarter".format(numberOfQuarters))

if numberOfDimes > 0:
    if numberOfDimes > 1:
        print("\t{} dimes".format(numberOfDimes))
    else:
        print("\t{} dime".format(numberOfDimes))

if numberOfNickels > 0:
    if numberOfNickels > 1:
        print("\t{} nickels".format(numberOfNickels))
    else:
        print("\t{} nickel".format(numberOfNickels))

if numberOfPennies > 0:
    if numberOfPennies > 1:
        print("\t{} pennies".format(numberOfPennies))
    else:
        print("\t{} penny".format(numberOfPennies))