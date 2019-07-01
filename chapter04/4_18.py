exchangeRate = eval(input("Enter the exchange rate from dollars to RMB: "))
status = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

if status == 0:
    dollarAmount = eval(input("Enter the dollar amount: "))
    print("${:.1f} is {:.2f} yuan".format(dollarAmount, dollarAmount * exchangeRate))
elif status == 1:
    rmbAmount = eval(input("Enter the RMB amount: "))
    print("{:.1f} yuan is ${:.2f}".format(rmbAmount, rmbAmount / exchangeRate))
else:
    print("Incorrect input")