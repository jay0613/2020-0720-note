"""
广播发送
1.创建udp套接字
2.设置套接字可以发送广播
3.循环向广播地址发送
"""
from socket import *
from time import sleep

# 广播地址
dest = ("127.0.0.1",8888)

# 创建套接字 ipV4   udp数据报套接字
s = socket(AF_INET, SOCK_DGRAM)

# 设置套接字接收发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

date = """
          ******************
            深圳 7.4 盛夏
            温度 22.5
            状态：没有四块五的妞
          ******************  
"""
while True:
    sleep(10)
    s.sendto(date.encode(),dest)  # 向dest地址发送date信息