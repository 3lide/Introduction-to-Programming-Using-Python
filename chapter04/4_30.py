import time

currentTime = time.time()
totalSeconds = int(currentTime)
currentSeconds = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinutes = totalMinutes % 60
totalHours = totalMinutes // 60
currentHours = totalHours % 24

timeZoneOffset = eval(input("Enter the time zone offsetto GMT: "))
currentHours = currentHours + timeZoneOffset

if currentHours > 12:
    currentHours -= 12

print("The current time is {}:{}:{}".format(currentHours, \
    currentMinutes, currentSeconds))