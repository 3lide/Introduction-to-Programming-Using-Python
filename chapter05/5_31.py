def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

#year是年份，month是月份，firstDay是该年一月份第一天是星期几，
#函数计算该年该月的第一天是该年的第几天
def getTotalDays(year, month, firstDay):
    totalDays = firstDay
    daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30]
    for i in range(month):
        totalDays += daysInMonth[i]
    if month > 2:
        if isLeapYear(year):
            totalDays += 1
    return totalDays

def dispalyCalender(year, month, firstDay):
    daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    monthDict = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, \
        "July":7, "August":8, "September":9, "October":10, "November":11, \
        "December":12}
    monthKey = tuple(monthDict.keys())
    print("{:>16s} {:<15d}".format(
        monthKey[tuple(monthDict.values()).index(month)], year))
    print("{:-^31s}".format('-'))
    print("  Sun Mon Tue Wed Thu Fri Sat  ")
    totalDays = getTotalDays(year, month, firstDay)
    days = totalDays % 7
    print("  ", end = "")
    for i in range(days):
        print(format(" ", ">3s"), end = " ")
    if month == 2 and isLeapYear(year):
        daysInMonth[1] = 29
    count = days
    for j in range(1, daysInMonth[month-1]+1):
        print(format(j, ">3d"), end = " ")
        count += 1
        if count == 7:
            print(" ")
            count = 0
            print("  ", end = "")
    print()

def main():
    year = eval(input("Enter the year: "))
    firstDay = eval(input("该年的第一天是星期几？(星期天-0，星期一-1，星期二-2，...，星期六-6): "))
    for i in range(12):
        dispalyCalender(year, i+1, firstDay)
    
if __name__ == "__main__":
    main()