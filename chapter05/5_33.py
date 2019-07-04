initAmount = eval(input("Enter the initial deposit amount: "))
annualPercentageYield = eval(input("Enter annual percentage yield: "))
maturityPeriod = eval(input("Enter maturity period (number of months): "))

monthlyPercentageYeild = annualPercentageYield / 1200

print("{:<5s}\t{:^8s}".format("Month", "CD Value"))
totalValue = initAmount
for i in range(maturityPeriod):
    totalValue = totalValue * (1 + monthlyPercentageYeild)
    print("{:<5d}\t{:^8.2f}".format(i+1, totalValue))