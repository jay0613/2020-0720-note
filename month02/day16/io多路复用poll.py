"""
poll实现多路服用
"""
from socket import *
from select import *

tcp_sock = socket()
tcp_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重用
tcp_sock.bind(("0.0.0.0",8888))
tcp_sock.listen(4)

p = poll()
map = {tcp_sock.fileno():tcp_sock}

p.register(tcp_sock,POLLIN)

while True:
    events = p.poll()
    for fd,event in events:
        if fd == tcp_sock.fileno():
            connfd,addr = map[fd].accept()
            p.register(connfd,POLLIN)
            map[connfd.fileno()] = connfd
            print("%s已连接"%str(addr))
        elif event == POLLIN:
            data = map[fd].recv(1024).decode()
            if not data:
                print("客户端退出！")
                p.unregister(map[fd])
                map[fd].close()
                del map[fd]
                continue
            print(data)
            p.register(map[fd],POLLOUT)
        elif event == POLLOUT:
            map[fd].send("收到消息".encode())
            p.register(map[fd],POLLIN)