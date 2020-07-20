"""
httpserver v1.0
基本要求： 1. 获取来自浏览器的请求
         2. 判断请求内容是否为/
         3. 如果是，则将 index.html 发送给浏览器
            如果不是，则告知浏览器 sorry
         4. 注意组织http响应格式， 判断 200 or 404
"""

from socket import *

# 处理客户端请求
def request(connfd):
    # 直接获取HTTP请求
    # 客户端连接上之后会发送请求过来
    data = connfd.recv(4096)
    # 防止浏览器断开
    if not data:
        return

    # 提取请求内容
    request_line = data.decode().split('\n')[0]  # 以\n作为分隔符，分成若干个元素，取第一个即可得到请求行
    info = request_line.split(' ')[1]  # 以空格作为分隔符把请求行分隔成若干个元素，获取第二个元素

    # 判断请求内容是否为 /
    if info == '/':
        with open('index.html') as f:
            response="HTTP/1.1 200 OK\r\n"
            response+="Content-Type:text/html\r\n"
            response+="\r\n"
            response+=f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry....</h1>"
    # 发送给浏览器
    connfd.send(response.encode())

# 搭建tcp服务
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)  # setsockopt设置端口重用
sockfd.bind(('0.0.0.0',8005))
sockfd.listen(5)
while True:
    connfd, addr = sockfd.accept()
    print("Connect from",addr)
    request(connfd)  # 具体处理客户端请求



