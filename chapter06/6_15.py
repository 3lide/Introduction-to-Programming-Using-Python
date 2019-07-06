def computeTax(status, taxableIncome):
    if status == 0:
        if taxableIncome <= 8350:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 33950:
            tax = 8350 * 0.10 + (taxableIncome - 8350) * 0.15
        elif taxableIncome <= 82250:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (taxableIncome - 33950) * 0.25
        elif taxableIncome <= 171550:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (82250 - 33950) * 0.25 + (taxableIncome - 82250) * 0.28
        elif taxableIncome <= 372950:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
                (taxableIncome - 171550) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
                (372950 - 171550) * 0.33 + (taxableIncome - 372950) * 0.35

    elif status == 1:
        if taxableIncome <= 16700:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 67900:
            tax = 16700 * 0.10 + (taxableIncome - 16700) * 0.15
        elif taxableIncome <= 137050:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                (taxableIncome - 67900) * 0.25
        elif taxableIncome <= 208850:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                (137050 - 67900) * 0.25 + (taxableIncome - 137050) * 0.28
        elif taxableIncome <= 372950:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
                (taxableIncome - 208850) * 0.33
        else:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
                (372950 - 208850) * 0.33 + (taxableIncome - 372950) * 0.35

    elif status == 2:
        if taxableIncome <= 8350:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 33950:
            tax = 8350 * 0.10 + (taxableIncome - 8350) * 0.15
        elif taxableIncome <= 68525:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (taxableIncome - 33950) * 0.25
        elif taxableIncome <= 104425:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (68525 - 33950) * 0.25 + (taxableIncome - 68525) * 0.28
        elif taxableIncome <= 186475:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
                (taxableIncome - 104425) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
                (186475 - 104425) * 0.33 + (taxableIncome - 186435) * 0.35

    elif status == 3:
        if taxableIncome <= 11950:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 45500:
            tax = 11950 * 0.10 + (taxableIncome - 11950) * 0.15
        elif taxableIncome <= 117450:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                (taxableIncome - 45500) * 0.25
        elif taxableIncome <= 190200:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                (117450 - 45500) * 0.25 + (taxableIncome - 117450) * 0.28
        elif taxableIncome <= 372950:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
                (taxableIncome - 190200) * 0.33
        else:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
                (372950 - 190200) * 0.33 + (taxableIncome - 372950) * 0.35

    return tax

def main():
    print('-'*104)
    print("{:^20s}|{:^20s}|{:^20s}|{:^20s}|{:^20s}".format(
        "Taxable Income", "Single", "Married Joint", "Married Separate", 
        "Head of a House"
    ))
    print('-'*104)
    for i in range(50000, 60001, 50):
        print("{:^20d}|{:^20d}|{:^20d}|{:^20d}|{:^20d}".format(
            i,
            int(computeTax(0, i)),
            int(computeTax(1, i)),
            int(computeTax(2, i)),
            int(computeTax(3, i))
        ))
        print('-'*104)

if __name__ == "__main__":
    main()