"""
chat room 群聊聊天室 udp客户端
发送请求，展示结果
"""

from socket import *
import os,sys

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 进入聊天室
def login(s):
    while True:
        try:   # 如果进程崩溃或者直接ctrl+C退出进程，则会运行except的内容退出进程，防止出错
            name = input("请输入昵称:")
            if not name:  # 如果不输入则结束本次循环继续while Ture循环，直到输入内容才会执行21行
                continue
        except KeyboardInterrupt:
            sys.exit("谢谢使用")
        msg = "L " + name  # L后面有个空格
        s.sendto(msg.encode(),ADDR)
        #　接收反馈结果
        data,addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            return name
        else:
            print(data.decode())

# 子进程函数
def send_msg(s,name):
    while True:
        try:  # 用了try进程，服务端崩溃或者ctrl+C关闭程序则会执行except代码，所以也会退出聊天室，如果崩溃没退出的话，用户名会永远存在服务端的字典里
            text = input("头像:")
        except KeyboardInterrupt:
            text = 'quit'
        # 退出聊天室  聊天窗口输入quit可以退出聊天室
        if text.strip() == 'quit':  # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）
            msg = "Q " + name
            s.sendto(msg.encode(),ADDR)
            sys.exit('退出聊天室')
        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        # 接收进程退出，若没退出则还可以接收到消息
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+'\n头像:',end='')  # 加了'\n头像:',end=''之后，每次接收到消息，自己的聊天输入会自动弹到下一行

# 客户端启动函数
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    name = login(s) # 请求进入聊天室

    # 创建新的进程
    pid = os.fork()
    if pid < 0:
        print("Error!!")
        return
    elif pid == 0:
        send_msg(s,name)  # 子进程发送消息
    else:
        recv_msg(s)  # 父进程接收消息

main()

