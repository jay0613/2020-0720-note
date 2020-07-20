"""
epoll实现多路服用
"""
from socket import *
from select import *

tcp_sock = socket()
tcp_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重用
tcp_sock.bind(("0.0.0.0",8888))
tcp_sock.listen(4)

ep = epoll()
map = {tcp_sock.fileno():tcp_sock}

ep.register(tcp_sock, EPOLLIN)

while True:
    events = ep.poll()
    for fd,event in events:
        if fd == tcp_sock.fileno():
            connfd,addr = map[fd].accept()
            ep.register(connfd, EPOLLIN)
            map[connfd.fileno()] = connfd
            print("%s已连接"%str(addr))
        elif event == EPOLLIN:
            data = map[fd].recv(1024).decode()
            if not data:
                print("客户端退出！")
                ep.unregister(map[fd])
                map[fd].close()
                del map[fd]
                continue
            print(data)
            ep.unregister(map[fd])
            ep.register(map[fd],EPOLLOUT)
        elif event == EPOLLOUT:
            map[fd].send("收到消息".encode())
            ep.unregister(map[fd])
            ep.register(map[fd], EPOLLIN)