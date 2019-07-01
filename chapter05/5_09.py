currentFee = 10000
growthRate = 0.05

feeIn10Years = currentFee * (1 + growthRate) ** 10

totalFee = 0
fee = feeIn10Years
for i in range(4):
    totalFee += fee
    fee = fee * (1 + growthRate)

print("十年后的学费为{:.2f}，从现在开始到十年后大学四年的总学费为{:.2f}". \
    format(feeIn10Years, totalFee))