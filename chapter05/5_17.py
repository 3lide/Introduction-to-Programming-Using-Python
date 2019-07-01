number1 = ord('!')
number2 = ord('~')

count = 0
for i in range(number1, number2+1):
    print(chr(i), end = ' ')
    count += 1
    if count == 10:
        print()
        count = 0
print()