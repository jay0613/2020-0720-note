from socket import socket

ADDR = ("127.0.0.1", 8885)

while 1:
    msg = input("请输入消息：")
    if msg=="":
        break
    # 创建tcp套接字
    tcp_socket = socket()
    # 连接服务的
    tcp_socket.connect(ADDR)
    # 发送消息
    tcp_socket.send(msg.encode())
    # 接收消息
    data = tcp_socket.recv(1024)
    print(data.decode())
    tcp_socket.close()
