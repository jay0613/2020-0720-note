"""
聊天室 客户端
"""
from socket import *
from multiprocessing import Process
import sys

ADDR = ("127.0.0.1", 8888)

def send_msg(sock,name):
    while True:
        msg = input("我：")

        if msg == "exit":
            content = "Q %s"%msg
            sock.sendto(content.encode(), ADDR)
            sys.exit("您已退出聊天室！")
        data = "C %s %s" %(name,msg)
        sock.sendto(data.encode(),ADDR)


def recv_msg(sock):
    while True:
        data,addr = sock.recvfrom(1024)
        print(data.decode())


def login(sock):
    while True:
        name = input("请输入昵称：")
        msg = "L " + name
        sock.sendto(msg.encode(),ADDR)
        result,addr = sock.recvfrom(1024)
        if result == b"OK":
            print("您已进入聊天室！")
            return name

        else:
            print("用户已存在")


def main():
    sock = socket(AF_INET,SOCK_DGRAM)  # udp
    name = login(sock)
    t = Process(target=recv_msg,args=(sock,))
    t.daemon = True
    t.start()
    send_msg(sock,name)


if __name__ == '__main__':
    main()