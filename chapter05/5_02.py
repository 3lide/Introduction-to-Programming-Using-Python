import random
import time

correctCount = 0
count = 0
NUMER_OF_QUESTIONS = 2

startTime = time.time()

while count < NUMER_OF_QUESTIONS:
    number1 = random.randint(1, 15)
    number2 = random.randint(1, 15)

    answer = eval(input("What is {} + {} ? ".format(number1, number2)))

    if answer == number1 + number2:
        print("You are correct!")
        correctCount += 1
    else:
        print("You are wrong.\n{} + {} = {}".format(number1, number2, \
            number1 + number2))
    count += 1

endTime = time.time()
testTime = int(endTime - startTime)

print("Correct count is", correctCount, "out of", NUMER_OF_QUESTIONS,
"\nTest time is", testTime, "seconds")