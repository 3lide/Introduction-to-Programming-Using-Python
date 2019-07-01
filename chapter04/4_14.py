import random

#0代表硬币正面，1代表反面
status = random.randint(0, 1)

number = eval(input("0代表硬币正面，1代表反面\n请输入你猜的数字: "))

if number == status:
    print("你猜对了")
else:
    print("你猜错了")