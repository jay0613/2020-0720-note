from socket import *
from select import select

#　创建监听套接字
tcp_sock = socket()
# tcp_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重用
# tcp_sock.bind(('0.0.0.0', 8888))
# tcp_sock.listen(5)
tcp_sock.connect(("127.0.0.1", 8888))
# tcp_sock.sendto(("127.0.0.1",8888))


while True:
    msg = input(">>>")
    tcp_sock.send(msg.encode())
    data = tcp_sock.recv(1024).decode()
    print(data)