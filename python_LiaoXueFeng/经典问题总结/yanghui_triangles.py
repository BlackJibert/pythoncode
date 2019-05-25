# 用python生成器实现杨辉三角
def triangles(line):
    l, index = [1], 0
    for i in range(line):
        yield l
        l = [1] + [l[i] + l[i + 1] for i in range(i + 1 - 1)] + [1]
        index += 1


for i in triangles(10):
    print(i)
