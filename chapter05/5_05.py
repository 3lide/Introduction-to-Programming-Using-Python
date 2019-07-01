print("公斤\t磅\t公斤\t磅")
for i in range(1, 101):
    index1 = 2 * (i -1) + 1
    index2 = 5 * (i -1) + 20
    print("{}\t{:.1f}\t{:.2f}\t{}".format(index1, index1 * 2.2, \
        index2 / 2.2, index2))