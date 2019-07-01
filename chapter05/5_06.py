print("英里\t公里\t英里\t公里")

for i in range(1, 11):
    index = 5 * (i -1) + 20
    print("{}\t{:.3f}\t{:.3f}\t{}".format(i, i*1.609, index / 1.609, index))