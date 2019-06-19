temperature = eval(input("Enter the temperature in Farenheit between \
-58 and 41: "))
windSpeed = eval(input("Enter the wind speed in miles per hour: "))

windChillIndex = 35.74 + 0.6215 * temperature - 35.75 * windSpeed ** 0.16 + \
    0.4275 * temperature * windSpeed ** 0.16

print("The wind chill index is", format(windChillIndex, ".5f"))