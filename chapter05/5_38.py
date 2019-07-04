import time

numberOfSeconds = eval(input("Enter the number of seconds: "))

if numberOfSeconds == 0:
    print("Stopped")
elif numberOfSeconds == 1:
    time.sleep(1)
    print("Stopped")
else:
    for i in range(numberOfSeconds-1, 1, -1):
        time.sleep(1)
        print("{} seconds remaining".format(i))
    time.sleep(1)
    print("1 second remaining")
    time.sleep(1)
    print("Stopped")