annualInterestRate = 0.05
numberOfYears = 5
loanAmount = 10000

monthlyInterestRate = annualInterestRate / 12
times = int((8 - 5) / 0.125)

print("{:^15s}\t{:^15s}\t{:^15s}".format("Interest Rate", "Monthly Payment", \
    "Total Payment"))
for i in range(times+1):
    monthlyPayment = loanAmount * monthlyInterestRate / (1 
        - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
    totalPayment = monthlyPayment * numberOfYears * 12
    print("{:^15.3%}\t{:^15.2f}\t{:^15.2f}".format(annualInterestRate, \
        monthlyPayment, totalPayment))
    annualInterestRate = (annualInterestRate * 100 + 0.125) / 100
    monthlyInterestRate = annualInterestRate / 12