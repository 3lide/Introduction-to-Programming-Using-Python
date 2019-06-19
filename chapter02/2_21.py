monthlySavingMoney = eval(input("Enter the monthly saving amount: "))
currentMoney = 0

for i in range(1, 7):
    currentMoney = (currentMoney + monthlySavingMoney) * ( 1 + 0.00417)

print("Aftr the sixth month, the account value is", format(currentMoney, ".2f"))