# 客户端
# !/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8000))
while True:
    msg = input(">>>:").strip()
    if not msg:
        continue
    # 发送给服务端的消息
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print('收到服务端发来的消息', data)
phone.close()
