"""
author: jie
email: yangchunyijie@163.com
time: 2020-7-16
env: Python3.6
socket and Process exercise
"""
from socket import *
from multiprocessing import Process
from signal import *

ADDR = ("0.0.0.0",8888)

#{用户名：address}
user = {}

class ChatProcess(Process):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            msg = data.decode().split(" ",2)
            if msg[0] == "L":
                self.login(msg[1],addr)
            elif msg[0] == "C":
                self.do_chat(msg[1],msg[2])
            elif msg[0] == "Q":
                self.do_exit(msg[1])

    def login(self, name, addr):
        if name in user:
            self.sock.sendto(b"FAIL",addr)
            return
        else:
            self.sock.sendto(b"OK",addr)
            for i in user:
                msg = "欢迎%s进入聊天室！"%name
                self.sock.sendto(msg.encode(), user[i])
            user[name] = addr

    def do_chat(self, name, content):
        msg = "%s : %s" %(name,content)
        print(user)
        for i in user:
            if i != name:
                self.sock.sendto(msg.encode(),user[i])

    def do_exit(self, name):
        del user[name]
        msg = "%s已退出群聊！"%name
        for i in user:
            self.sock.sendto(msg.encode(), user[i])



def main():
    sock = socket(AF_INET, SOCK_DGRAM)  # udp套接字
    sock.bind(ADDR)
    t = ChatProcess(sock)
    t.daemon=True  # 父进程退出 子进程全部退出
    signal(SIGCHLD,SIG_IGN)   # 子进程退出自动交给系统处理 不会变僵尸
    t.start()

    while True:
        msg = input("管理员消息：")

main()