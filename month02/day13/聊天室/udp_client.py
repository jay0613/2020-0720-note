from socket import *
from multiprocessing import *

ADDR = ("127.0.0.1",8888)
sockfd = socket(AF_INET,SOCK_DGRAM)

def recv():
    while True:
        data, addr = sockfd.recvfrom(1024)
        print(data.decode())

while True:
    number = input("请输入数字(注册1 / 登录2)：")
    if number == "1":
        name1 = input("请输入注册用户：")
        name = name1+"##"
        sockfd.sendto(name.encode(),ADDR)
        data,addr = sockfd.recvfrom(1024)
        if data.decode() == "ok":
            print("注册成功!")
            continue
        elif data.decode() == "o":
            print("用户已存在，请重新注册！")
    elif number == "2":
        name = input("请输入用户名：")
        sockfd.sendto(name.encode(), ADDR)
        data, addr = sockfd.recvfrom(1024)
        if data.decode() == "ok":
            print("登录成功！")
            continue
    else:
        "请输入数字1或者2！"

p = Process(target=recv)
p.start()
while True:
    data = input(">>>")
    sockfd.sendto(data.encode(),ADDR)
