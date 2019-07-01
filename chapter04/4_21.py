#输入年份
year = eval(input("Enter year: (e.g., 2008): "))
#输入月份
month = eval(input("Enter month: 1-12: "))
#输入具体日期
dayOfTheMonth = eval(input("Enter the day of the month: 1-31: "))

#判断是否为1、2月，如果是将月份加上12，年份减1
if month in [1, 2]:
    month = month + 12
    year = year - 1

#计算输入年份的世纪数和所在世纪的年数
century = year // 100
numberOfYear = year % 100

date = (dayOfTheMonth + (26 * (month + 1)) // 10 + numberOfYear + \
    numberOfYear // 4 + century // 4 + 5 * century) % 7

if date == 0:
    print("Day of the week is Saturday.")
elif date == 1:
    print("Day of the week is Sunday.")
elif date == 2:
    print("Day of the week is Monday.")
elif date == 3:
    print("Day of the week is Tuesday.")
elif date == 4:
    print("Day of the week is Wednesday.")
elif date == 5:
    print("Day of the week is Thursday.")
else:
    print("Day of the week is Friday.")