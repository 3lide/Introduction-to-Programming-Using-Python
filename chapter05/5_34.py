import random

lotteryDigit1 = random.randint(1,9)
lotteryDigit2 = random.randint(0,9)
while lotteryDigit2 == lotteryDigit1:
    lotteryDigit2 = random.randint(0,9)
lottery = lotteryDigit1 * 10 + lotteryDigit2

guess = eval(input("Enter your lottery pick (two digits): "))

guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)

if guess == lottery:
    print("Exact match: you win $10000")
elif guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2:
    print("Match all digits: you win $3000")
elif guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2 or \
    guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2:
    print("Match one digit: you win $1000")
else:
    print("Sorry, no match")