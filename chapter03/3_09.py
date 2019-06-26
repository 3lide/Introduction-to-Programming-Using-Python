name = input("Enter employee's name: ")
numberOfHours = eval(input("Enter number of hours worked in a week: "))
hourlyPayRate = eval(input("Enter hourly pay rate: "))
federalTaxWithholdingRate = eval(input("Enter federal tax withholding rate: "))
stateTaxWithholdingRate = eval(input("Enter state tax withholding rate: "))

grossPay = numberOfHours * hourlyPayRate
federalWithholding = grossPay * federalTaxWithholdingRate
stateWithholding = grossPay * stateTaxWithholdingRate
totalDeduction = federalWithholding + stateWithholding
netPay = grossPay - totalDeduction

print("Employee Name:", name, "\n", 
    "Hours Worked: {:.1f}".format(numberOfHours), "\n",
    "Pay Rate: ${:.2f}".format(hourlyPayRate), "\n",
    "Gross Pay: ${:.1f}".format(grossPay), "\n", 
    "Deductions:", "\n", 
    "\t", "Federal Withholding ({:.1%}): ${:.1f}".format( \
        federalTaxWithholdingRate, federalWithholding), "\n", 
    "\t", "State Withholding ({:.1%}): ${:.2f}".format( \
        stateTaxWithholdingRate, stateWithholding), "\n", 
    "\t", "Total Deduction: ${:.2f}".format(totalDeduction), "\n", 
    "Net Pay: ${:.2f}".format(netPay))