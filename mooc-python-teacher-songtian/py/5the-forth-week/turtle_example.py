import turtle


def drawline(draw):  # 绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
    # 行进40像素，并转90度


drawline(1)
