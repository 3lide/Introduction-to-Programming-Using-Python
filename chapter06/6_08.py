def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32

def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

print('-'*121)
print("{:^29s}|{:^29s}| |{:^29s}|{:^29s}".format("Celsius", "Fahrenheit", \
    "Fahrenheit", "Celsius"))
print('-'*121)
for i in range(10, 0, -1):
    print("{:^29.1f}|{:^29.1f}|".format(30+i, celsiusToFahrenheit(30+i)), 
    end = ' ')
    print("|{:^29.1f}|{:^29.2f}".format(10*i+20, fahrenheitToCelsius(10*i+20)))

print('-'*121)