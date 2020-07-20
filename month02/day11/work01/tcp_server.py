"""
     从客户端指定一张图片，将其传输到服务端
     在服务端以 日期为图片名称存储

   比如： 客户端有一张  xxxxx.jpg
         传到服务端存为   2020-7-10.jpg
"""
from socket import *
ADDR = ("0.0.0.0",8888)
tcp_socket = socket()
# 设置端口立即重用，端口立刻断开，防止上一次的没断开，会造成端口被占用情况
tcp_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)   # 只要记住SOL_SOCKET就可以了，SO_REUSEADDR为SOL_SOCKET类别下的一个具体功能，第三个参数为True时候执行该功能

tcp_socket.bind(ADDR)
tcp_socket.listen(5)
connfd,addr = tcp_socket.accept()
print(addr,"连接进来了")
f = open("2020-7-10.jpg","ab+")
while True:
    data = connfd.recv(1024)
    if not data:
        break
    f.write(data)
tcp_socket.close()
