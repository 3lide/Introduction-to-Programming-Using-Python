import math

total = 0
for i in range(1, 625):
    total += 1 / (math.sqrt(i) + math.sqrt(i+1))
print(total)