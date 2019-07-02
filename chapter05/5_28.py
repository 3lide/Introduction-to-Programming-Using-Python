e = 1
temp = 1
n = eval(input("Enter n: "))
for i in range(1, n+1):
    temp *= i
    e += 1 / temp

print(e)