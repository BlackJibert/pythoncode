import turtle as t

t.title("自动轨迹绘制")
# t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)
# 数据读取
datails = []
f = open("data.txt")
for line in f:
    # print(line)
    line = line.replace("\n", "")
    # map函数的功能将第一个参数的功能作用于第二个参数的每一个元素
    datails.append(list(map(eval, line.split(","))))

f.close()
# 自动绘制
for i in range(len(datails)):
    t.pencolor(datails[i][3], datails[i][4], datails[i][5])
    t.fd(datails[i][0])  # 行进多少像素
    # 转向
    if datails[i][1]:
        t.right(datails[i][2])
    else:
        t.left(datails[i][2])
