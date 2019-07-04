count = 0
for i in range(1, 7):
    for j in range(i+1, 8):
        print(i,j)
        count += 1
print("The total number of all combinations is", count)