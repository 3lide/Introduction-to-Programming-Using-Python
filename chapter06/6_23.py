def convertMillis(millis):
    totalseconds = millis // 1000
    seconds = totalseconds % 60
    totalMinutes = totalseconds // 60
    minutes = totalMinutes % 60
    totalhours = totalMinutes // 60
    hours = totalhours % 24
    return "{}:{}:{}".format(hours, minutes, seconds)

print(convertMillis(5500))