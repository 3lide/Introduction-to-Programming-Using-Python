finalAccount = eval(input("Enter the final account value: "))
annualInterestRate = eval(input("Enter annua interest rate in percent: "))
numberOfYears = eval(input("Enter number of years: "))

monthlyInterestRate = annualInterestRate / 12
numberOfMonth = numberOfYears * 12

initialDepositValue = finalAccount / (1 + monthlyInterestRate / 100) ** \
    numberOfMonth

print("Initial deposit value is", initialDepositValue)