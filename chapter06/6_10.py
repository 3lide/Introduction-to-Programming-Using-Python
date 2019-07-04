def isPrimer(number):
    if number == 1:
        return False
    else:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                return False
        return True

def main():
    count = 0
    for i in range(1, 10000):
        if isPrimer(i):
            count += 1
    print("小于10000的素数个数为：",count)

if __name__ == "__main__":
    main()