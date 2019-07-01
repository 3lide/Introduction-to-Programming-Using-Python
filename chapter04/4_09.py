weight1, price1 = eval(input(
    "Enter weight and price for package 1: "
))
weight2, price2 = eval(input(
    "Enter weight and price for package 2: "
))

#计算单价
priceForP1 = price1 / weight1
priceForP2 = price2 / weight2

if priceForP1 > priceForP2:
    print("Package 2 has better price.")
else:
    print("Package 1 has better price.")