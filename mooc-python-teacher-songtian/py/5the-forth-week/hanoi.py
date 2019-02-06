count = 0


# count用来记录步数
def hanoi(n, src, dst, mid):
    # n个圆盘，从src(A),经mid(B)，搬到C。注意：柱子始终有序。
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    # 若只有一个圆盘，之间将其从A搬到C
    else:
        hanoi(n - 1, src, mid, dst)
        # 先将n-1个柱子，从src经dst,搬到mid.
        print("{}:{}->{}".format(n, src, dst))
        # 把第n个柱子(最大的柱子)从src搬到dst
        count += 1
        hanoi(n - 1, mid, dst, src)
        # 然后把n-1个柱子从中间柱子mid，经src,搬到dst.


hanoi(3, "A", "C", "B")
print(count)
