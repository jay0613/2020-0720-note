from socket import socket

ADDR = ("0.0.0.0", 8888)
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

        # 接收客户端消息
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send("发送成功".encode())

    connfd.close()



