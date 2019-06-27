def main():
    today = eval(input("Enter today's day: "))
    numberOfDays = eval(input("Enter the number of days elapsed since today: "))
    futureDay = today + numberOfDays
    print("Today is {} and the future day is {}".format(whichDay(today), \
        whichDay(futureDay)))

def whichDay(number):
    number = number % 7
    if number == 0:
        date = "Sunday"
    elif number == 1:
        date = "Monday"
    elif number == 2:
        date = "Tuesday"
    elif number == 3:
        date = "Wedensday"
    elif number == 4:
        date = "Thursday"
    elif number == 5:
        date = "Friday"
    else:
        date = "Saturday"
    return date

if __name__ == "__main__":
    main()