filePath = "/home/wangheng/Desktop/code/Introduction to Programming Using Python/\
chapter05/score.txt"
#读取文件内容
file = open(filePath)
number = file.readlines()

#去掉换行符
inputValue = []
for line in number:
    inputValue.append(line.strip('\n'))

studentsNumber = eval(inputValue[0])
score = inputValue[1:]

highestScore = 0
for i in range(studentsNumber):
    if highestScore < eval(score[i]):
        highestScore = eval(score[i])

print("The highest score is", highestScore)