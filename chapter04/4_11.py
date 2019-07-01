#判断是否为闰年
def isLeapYear(year):
    if (year % 100 != 0 and year % 4 ==0) or year % 400 ==0:
        return True
    else:
        return False

def main():
    #输入年份和月份
    year = eval(input("Enter year: "))
    month = eval(input("Enter month: "))

    #保证月份正确，在1-12之间，防止输入错误
    while True:
        if month < 1 or month > 12:
            print("Mont should between 1 and 12, please enter month again: ")
            month = eval(input("Enter month again: "))
        else:
            break

    if month in [1, 3, 5, 7, 8, 10, 12]:
        daysOfMonth = 31
    if month == 2:
        if isLeapYear(year):
            daysOfMonth = 29
        else:
            daysOfMonth = 28
    if month in [4, 6, 9, 11]:
        daysOfMonth = 30
    
    print("{}年{}月份有{}天。".format(year, month, daysOfMonth))

if __name__ == "__main__":
    main()