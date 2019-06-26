amount = eval(input("Enter an amount, for example, 1156(express 11 dollars and 56 cents):"))

numberOfDollars = amount // 100
remainingAmount = amount % 100

numberOfQuaters = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfPennies = remainingAmount

print("Your amount", amount, "consist of\n",
    "\t", numberOfDollars, "dollars\n",
    "\t", numberOfQuaters, "quaters\n",
    "\t", numberOfDimes, "dimes\n",
    "\t", numberOfNickels, "nickels\n",
    "\t", numberOfPennies, "pennies")