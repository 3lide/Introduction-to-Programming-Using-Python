def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

count = 0
for i in range(2001, 2101):
    if isLeapYear(i):
        print(i, end = ' ')
        count += 1
        if count == 10:
            print()
            count = 0

print()