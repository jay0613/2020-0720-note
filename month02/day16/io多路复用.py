from socket import *
from select import select

#　创建监听套接字
tcp_sock = socket()
tcp_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重用
tcp_sock.bind(('0.0.0.0', 8888))
tcp_sock.listen(5)

udp_sock = socket(AF_INET, SOCK_DGRAM)
# data,addr = udp_sock.recvfrom(1024)


#　设置关注的ＩＯ列表
rlist = [tcp_sock,udp_sock]  # ｓ用于等待处理连接   # 读事件
wlist = [udp_sock]  # 写事件
xlist = []  # 出错事件，这个列表里面关注的事件出错的话就会返回给xs

#　循环ＩＯ监控
while True:
    # print("++++",rlist)
    rs,ws,xs = select(rlist,wlist,xlist,3)  # 返回值rs是一个列表，如果有客户端连接s,则返回s在rs列表内，如果有客户端发消息则会返回C在rs列表内
    print("rs:",rs)
    print("ws:",ws)
    print("xs:",xs)

