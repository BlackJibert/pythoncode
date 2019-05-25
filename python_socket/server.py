import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(('127.0.0.1', 8000))  # 绑定手机卡
phone.listen(5)
print('---------')
while True:
    conn, addr = phone.accept()  # 等电话

    print("电话线路是", conn)
    print("客户端的手机号是", addr)
    while True:  # 通讯循环
        try:
            msg = conn.recv(1024)  # 收消息
            if not msg:
                break
            print('客户端发来的消息是：', msg)
            conn.send(msg.upper())  # 发消息
        except Exception:
            break
    conn.close()
phone.close()
