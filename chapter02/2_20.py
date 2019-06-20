balance, interestRate = eval(input("Enter blance and interest rate(e.g., \
for 3%): "))

interest = balance * (interestRate / 1200)

print("The interest is", format(interest, ".5f"))