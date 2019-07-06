def isDoublePrime(number):
    if isPrime(number) and isPrime(number+2):
        return True

def isPrime(number):
    if number == 1:
        return False
    else:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                return False
        return True

def main():
    for i in range(1, 998):
        if isDoublePrime(i):
            print((i, i+2))

if __name__ == "__main__":
    main()