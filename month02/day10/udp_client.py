from socket import *

ADDR = ("127.0.0.1",8888)
while True:
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    word = input("请输入查询的单词(#退出)：")
    udp_socket.sendto(word.encode(),ADDR)
    if word == "#":
        break
    data,addr = udp_socket.recvfrom(1024)
    print("%s : %s"%(word,data.decode()))

udp_socket.close()
