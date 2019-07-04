for number in range(1, 10001):
    factor = []
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            factor.append(i)
    if number == sum(factor):
        print(number)