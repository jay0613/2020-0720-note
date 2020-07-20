from socket import socket
import time
ADDR = ("0.0.0.0", 8887)
# 创建tcp套接字
tcp_socket = socket()

# 绑定地址
tcp_socket.bind(ADDR)

# 设置成监听套接字
tcp_socket.listen(5)

# 阻塞等待客户端连接
while True:
    connfd, addr = tcp_socket.accept()
    print(addr, "连接进来了")

    while True:
        dict01 = {"几岁":"我2岁啦",
                  "男":"我是机器人，没有性别之分",
                  "几点":time.ctime()
                  }
        # 接收客户端消息
        data = connfd.recv(1024)
        if not data:
            break
        for key in dict01:
            if key in data.decode():

                msg = str(dict01[key])

                connfd.send(msg.encode())

    connfd.close()



