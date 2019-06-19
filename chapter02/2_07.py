totalMinutes = eval(input('Enter the number of minutes: '))

mininutesOfOneDay = 24 * 60

totalDays = totalMinutes // mininutesOfOneDay
years = totalDays // 365
days = totalDays % 365

print("{} minutes is approximately {} years and {} days.". \
    format(totalMinutes, years, days))