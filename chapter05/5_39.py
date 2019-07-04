basicWage = 5000
salesVolume = 0
totalPay = 5000

while totalPay < 30000:
    salesVolume += 1
    if salesVolume <= 5000:
        totalPay = basicWage + salesVolume * 0.08
    elif salesVolume <= 10000:
        totalPay = basicWage + 5000 * 0.08 + \
            (salesVolume - 5000) * 0.1
    else:
        totalPay = basicWage + 5000 * 0.08 + \
            5000 * 0.1 + (salesVolume - 10000) * 0.12
print("最小销售额为：", salesVolume)