"""
广播接收
1.创建udp套接字
2.设置套接字可以接收广播  （setsockopt）
3.选择接收的端口
4.接收广播
"""

from socket import *

# 创建套接字 ipV4   udp数据报套接字
s = socket(AF_INET, SOCK_DGRAM)

# 设置套接字接收发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)  # SO_BROADCAST表示套接字可以接收广播  1代表True

s.bind(("0.0.0.0", 8888))

while True:
    msg, addr = s.recvfrom(1024)  # 接收信息
    print(msg.decode())
