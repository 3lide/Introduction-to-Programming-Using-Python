innvestmentAMount = eval(input("Enter the investment amount: "))
annualInterestRate = eval(input("Enter annual interest rate: "))
numberOfYears = eval(input("Enter number of years: "))

monthlyInterestRate = annualInterestRate / 12
numberOfMonth = numberOfYears * 12

accumulatedValue = innvestmentAMount * (1 + \
    monthlyInterestRate / 100) ** numberOfMonth

print("Accumulated value is", format(accumulatedValue, ".2f"))