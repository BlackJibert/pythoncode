# C = ( F - 32 ) / 1.8‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬
# F = C * 1.8 + 32‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬

def tempConvert():
    t = input("请输入数值:")
    R = ["RMB", "rmb"]
    U = ["USD", "usd"]
    if t[0:3] in R:
        temp = float(t[3:]) / 6.78
        # print(temp)
        temp = "{:.2f}".format(temp)
        temp = "USD" + str(temp)
        print("结果：", temp)
    elif t[0:3] in U:
        temp = float(t[3:]) * 6.78
        temp = "{:.2f}".format(temp)
        temp = "RMB" + str(temp)
        print("结果：", temp)
    else:
        print("输入格式错误")
        return False
    return temp


tempConvert()
