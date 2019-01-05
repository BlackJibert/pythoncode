def sequential(x):
    a = [1, 2, 4, 3, 9, 5, 6, 7]
    sign = False
    for i in range(len(a)):
        if a[i] == x:
            print("exist %d,in %d" % (x, x + 1))
            sign = True
    if sign == False:
        print("no exist %d" % (x))


sequential(61)
