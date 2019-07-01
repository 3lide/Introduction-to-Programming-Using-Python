#定义寻找列表最大值的函数，参数number的元素为字符串，类型为列表
def findLargestNumber(number):
    largestNumber = 0
    length = len(number)
    for i in range(length):
        if largestNumber < eval(number[i]):
            largestNumber = eval(number[i])
    return largestNumber

filePath = "/home/wangheng/Desktop/code/Introduction to Programming Using Python/\
chapter05/score.txt"
#读取文件内容
file = open(filePath)
number = file.readlines()

#去掉换行符
inputValue = []
for line in number:
    inputValue.append(line.strip('\n'))

score = inputValue[1:]
firstHighestScore = findLargestNumber(score)
score.remove(str(firstHighestScore))
secondHighestScore = findLargestNumber(score)
print("最高分是{}，第二高分是{}".format(firstHighestScore, secondHighestScore))