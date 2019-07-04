def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate) ** \
        (years * 12)
    return futureInvestmentValue

investmentValue = eval(input("Enter investment value: "))
annualInterestRate = eval(input("Enter annual interest rate (for example:5): "))

print("{:^5s}\t{:^12s}".format("Years", "Future Value"))
for i in range(30):
    print("{:<5d}\t{:>12.2f}".format(i+1, futureInvestmentValue(investmentValue, 
        annualInterestRate / 1200, i+1)))