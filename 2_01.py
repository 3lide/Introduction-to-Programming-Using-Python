degreeInCelsius = eval(input('Enter a degree in Celsius: '))

fahrenheit = degreeInCelsius * (9 / 5)  + 32

print("{} Celsius is {:.1f} Fahrenheit.".format(degreeInCelsius, fahrenheit))