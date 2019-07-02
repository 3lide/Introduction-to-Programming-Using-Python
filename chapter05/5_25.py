n = 50000

sum1 = 0
for i in range(1, n+1):
    sum1 += 1 / i

sum2 = 0
for j in range(n, 0, -1):
    sum2 += 1 / j

print(sum1, sum2)