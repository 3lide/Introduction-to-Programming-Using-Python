def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def getDate(totalDays):
    day = totalDays % 7
    if day == 0:
        date = "Sunday"
    elif day == 1:
        date = "Monday"
    elif day == 2:
        date = "Tuesday"
    elif day == 3:
        date = "Wednesday"
    elif day == 4:
        date = "Thursday"
    elif day == 5:
        date = "Friday"
    elif day == 6:
        date = "Saturday"

    return date

year = eval(input("Enter the year: "))
day = eval(input("该年的第一天是星期几？(星期天-0，星期一-1，星期二-2，...，星期六-6): "))

month = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, \
    "July":7, "August":8, "September":9, "October":10, "November":11, \
    "December":12}
monthKey = tuple(month.keys())

totalDays = day
for i in range(1,13):
    date = getDate(totalDays)
    print("{} 1, {} is {}".format(monthKey[tuple(month.values()).index(i)], \
        year, date))
    if i in [1,3,5,7,8,10,12]:
        totalDays += 31
    elif i == 2:
        if isLeapYear(year):
            totalDays += 29
        else:
            totalDays += 28
    else:
        totalDays += 30
    

    