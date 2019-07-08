import time

def getCurrentTime():
    totalSeconds = int(time.time())
    second = totalSeconds % 60
    totalMinutes = totalSeconds // 60
    minute = totalMinutes % 60
    totalHours = totalMinutes // 60
    hour = totalHours % 24
    totalDays = totalHours // 24
    return hour, minute, second, totalDays

def isLeapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

def getDate(totalDays):
    year = 1970
    while True:
        if isLeapYear(year):
            totalDays -= 366
        else:
            totalDays -= 365
        year += 1
        if isLeapYear(year):
            if totalDays <= 366:
                break
        else:
            if totalDays <= 365:
                break
    month, day = getMonthAndDay(totalDays, year)
    return year, month, day


def getMonthAndDay(totalDays, year):
    monthDict = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, \
        'June':6, 'July':7, 'August':8, 'september':9, 'October':10, \
        'November':11, 'December':12}
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    i = 1
    if isLeapYear(year):
        daysInMonth[1] = 29
    while True:
        if totalDays <= sum(daysInMonth[0:i]):
            month = i
            break
        else:
            i += 1
    
    month = tuple(monthDict.keys())[tuple(monthDict.values()).index(month)]
    day = totalDays - sum(daysInMonth[0:i-1])
    return month, day

def main():
    hour, minute, second, totalDays = getCurrentTime()
    year, month, day = getDate(totalDays)
    print("Current date and time is {} {}, {} {}:{}:{}".format(
        month, day, year, hour, minute, second
    ))

if __name__ == "__main__":
    main()