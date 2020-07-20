"""
chat room  群聊聊天室  服务端
env: python3.6
socket udp & fork
未解决问题：服务端崩溃，已经登录的用户没退出
"""
from socket import *
import os,sys

# 服务端地址
ADDR = ('0.0.0.0',8888)
# 存储用户的结构 {name:address}
user = {}

# 处理登录
def do_login(s,name,addr):
    if name in user or '管理员' in name:  # 如果输入的name已经在user里，或者名字包含"管理员"
        s.sendto("该用户存在".encode(),addr)
        return

    # 加入用户
    msg = "\n欢迎 %s 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])  # user是字典，遍历字典得到键，所以i是键，所以user[i]是值，即是地址
    user[name] = addr  # 字典的添加内容方法：若字典里没有name，则添加name：addr
    s.sendto(b'OK',addr)

# 聊天
def do_chat(s,name,text):
    msg = "\n%s: %s"%(name,text)
    for i in user:
        # 刨除本人
        if i != name:
            s.sendto(msg.encode(),user[i])


# 退出
def do_quit(s,name):
    msg = "\n%s 退出聊天室"%name
    for i in user:
        if i != name:  # 刨除本人
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[i])
    del user[name]  # 删除该用户


# 接受请求，分发给不同方法处理
def do_request(s):
    while True:
        # 循环接收来自客户端及管理员的请求
        data,addr = s.recvfrom(1024)
        tmp = data.decode().split(' ',2)  # split（）以空格作为分隔符，分割成（2+1）个
        # 根据不同的请求类型分发函数处理
        # L 进入  C 聊天 Q退出
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr)
        elif tmp[0] == 'C':
            do_chat(s,tmp[1],tmp[2])
        elif tmp[0] == 'Q':
            if tmp[1] in user:
                do_quit(s, tmp[1])

# 搭建网络
def main():
    # udp服务端
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    # 开辟新的进程处理管理员消息
    pid = os.fork()
    if pid < 0:
        print("Error!!")
        return
    elif pid == 0:
        # 子进程处理管理员消息
        # 注意：fork()会复制父进程生成一个子进程，包括上面的user = {}，所以子进程不能会父进程里面的user = {}操作
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(),ADDR)  # 发送内容给自己，recvfrom接收后执行转发给各个客户端
    else:
        do_request(s) # 父进程处理客户端请求

main()
