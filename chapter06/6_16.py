def numberOfDaysInAYear(year):
    return 366 if isLeapYear(year) else 365

def isLeapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

def main():
    for year in range(2010, 2021):
        print("{}年有{}天".format(year, numberOfDaysInAYear(year)))

if __name__ == "__main__":
    main()