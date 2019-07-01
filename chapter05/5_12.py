#定义函数判断一个数是否能被5和6同时整除
def isDivisible(number):
    if number % 5 == 0 and number % 6 == 0:
        return True
    else:
        return False

count = 0
for i in range(100, 1001):
    if isDivisible(i):
        print(i, end = " ")
        count += 1
    if count == 10:
        print()
        count = 0

print()