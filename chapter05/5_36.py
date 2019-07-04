import random

computerWinCount = 0
userWinCount = 0
while computerWinCount < 2 and userWinCount < 2:
    computerNumber = random.randint(0, 2)

    userNumber = eval(input("scissor (0), rock (1), paper (2): "))

    if computerNumber == 0:
        if userNumber == 1:
            print("The computer is scissor. You are rock. You won.")
            userWinCount += 1
        elif userNumber == 0:
            print("The computer is scissor. You are scissor too. It is a draw.")
        elif userNumber == 2:
            print("The computer is scissor. You are paper. You defeated.")
            computerWinCount += 1

    elif computerNumber == 1:
        if userNumber == 0:
            print("The computer is rock. You are sicissor. You defeated.")
            computerWinCount += 1
        elif userNumber == 1:
            print("The computer is rock. You are rock too. It is a draw.")
        elif userNumber == 2:
            print("The computer is rock. You are paper. You won.")
            userWinCount += 1

    elif computerNumber == 2:
        if userNumber == 0:
            print("The computer is paper. You are scissor. You won.")
            userWinCount += 1
        elif userNumber == 1:
            print("The computer is paper. You are rock. You defeated.")
            computerWinCount += 1
        elif userNumber == 2:
            print("The computer is paper. You are paper too. It is a draw.")

    print("You won {} times, and computer won {} times".format(userWinCount, \
        computerWinCount)) 