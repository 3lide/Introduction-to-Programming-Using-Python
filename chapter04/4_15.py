import random

#Generate a lottery number
lottery = random.randint(100, 999)

#Prompt user to enter a number
number = eval(input("Enter your lottery pock (three digits): "))

#Get digits from lottery
lotteryString = list(str(lottery))
lotteryDigit1 = eval(lotteryString[0])
lotteryDigit2 = eval(lotteryString[1])
lotteryDigit3 = eval(lotteryString[2])

print("The lottery number is",lottery)

#Get digits from number
numberString = list(str(number))
numberDigit1 = eval(numberString[0])
numberDigit2 = eval(numberString[1])
numberDigit3 = eval(numberString[2])

#check the guess
if lotteryDigit1 == numberDigit1 and lotteryDigit2 == numberDigit2 and \
    lotteryDigit3 == numberDigit3:
    print("三个数字完全匹配，包括顺序，你赢得了{}美元。".format(10000))
elif str(lotteryDigit1) in numberString and str(lotteryDigit2) in numberString and \
    str(lotteryDigit3) in numberString:
    print("三个数字完全匹配，但是顺序不匹配，你赢得了{}美元。",format(3000))
elif str(lotteryDigit1) in str(numberDigit1) or lotteryDigit2 in numberString or \
    str(lotteryDigit3) in numberString:
    print("你输入的数字有1个或2个匹配，你赢得了{}美元。".format(1000))
else:
    print("你一个数字都没有猜中，所以没有奖金。")