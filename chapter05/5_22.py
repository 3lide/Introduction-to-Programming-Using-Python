def isPrimer(number):
    divisor = int(number / 2)
    while divisor >= 2:
        if number % divisor == 0:
            return False
        else:
            divisor -= 1
    return True

count = 0
for i in range(2, 1001):
    if isPrimer(i):
        print(format(i, ">3d"), end = ' ')
        count += 1
        if count == 8:
            print()
            count = 0