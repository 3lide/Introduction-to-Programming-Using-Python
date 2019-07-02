n = eval(input("Enter n: "))
pi = 0
for i in range(1, n+1):
    pi += (-1) ** (i+1) / (2 * i -1)

pi = 4 * pi
print(pi)