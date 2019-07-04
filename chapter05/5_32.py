amount = eval(input("请输入每月存储金额： "))
annualInterestRate = eval(input("请输入年利率： "))
months = eval(input("请输入存储月数： "))

totalAmount = 0
for i in range(months):
    totalAmount = (amount + totalAmount) * (1 + annualInterestRate / 1200)

print("{}个月后储蓄账户上的总金额为{:.2f}".format(months, totalAmount))