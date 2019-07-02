loanAmount = eval(input("Enter loan amount: "))
numberOfYears = eval(input("Enter the number of years: "))
annualInterestRate = eval(input("Enter annual interest rate: "))

monthlyInterestRate = annualInterestRate / 1200
monthlyPayment = loanAmount * monthlyInterestRate / (1 
    - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12
print("Monthly Payment:", format(monthlyPayment, ".2f"))
print("Total Payment:", format(totalPayment, ".2f"))

print("{:<10s}\t{:<10s}\t{:<10s}\t{:>10s}".format("Payment#", "Interest", \
    "Principal", "Balance"))

balance = loanAmount
for i in range(1, numberOfYears * 12 + 1):
    interest = balance * monthlyInterestRate
    principal = monthlyPayment - interest
    balance = balance - principal
    print("{:<10d}\t{:^10.2f}\t{:<10.2f}\t{:>10.2f}".format(i, \
        interest, principal, balance))