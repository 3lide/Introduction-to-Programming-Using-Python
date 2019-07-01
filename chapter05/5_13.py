#定义函数判断一个数是否可以被5或者6整除但是不能被二者同时整除
def isDivisible(number):
    if number % 5 == 0 or number % 6 == 0 and \
        ~(number % 5 == 0 and number % 6 == 0):
        return True
    else:
        return False

count = 0
for i in range(100, 201):
    if isDivisible(i):
        print(i, end = ' ')
        count += 1
    if count == 10:
        print()
        count = 0

print()