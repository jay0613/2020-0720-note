from socket import socket

ADDR = ("127.0.0.1", 8887)

# 创建tcp套接字
tcp_socket = socket()

# 连接服务的
tcp_socket.connect(ADDR)

while 1:

    # 发送消息
    msg = input("请输入消息：")
    if msg=="":
        break
    tcp_socket.send(msg.encode())


    # 接收消息
    data = tcp_socket.recv(1024)
    print(data.decode())

tcp_socket.close()