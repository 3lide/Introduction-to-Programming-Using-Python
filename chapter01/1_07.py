count = eval(input("Enter an integer: "))
pi = 0
for i in range(1,count + 1):
	pi = pi + pow(-1, i -1) * (1 / (2 * i - 1))
	
pi = 4 * pi

print("pi =",pi)
