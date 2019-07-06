def isPrime(number):
    if number == 1:
        return False
    else:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                return False
        return True

def main():
    print("{:^5s}\t{:^5s}".format("p", "2^p-1"))
    for p in range(1, 32):
        if isPrime(2**p-1):
            print("{:^5d}\t{:^5d}".format(p, 2**p-1))

if __name__ == "__main__":
    main()