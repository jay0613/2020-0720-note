"""
http响应过程演示
服务端
客户端一般是浏览器
输入ip地址即可访问（ip地址为英文格式）
"""

from socket import *

# tcp套接字 （http-->tcp）
s = socket()  # 创建套接字
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重用

s.bind(('0.0.0.0',8001))  # 绑定地址
s.listen(3)  # 设置监听

c, addr = s.accept()  # C返回的为客户端的套接字，adde为返回的连接的客户端地址
print("Connect from", addr)
# 获取请求
data = c.recv(4096).decode()
print(data)

# 返回响应
# 响应行 #响应头 #空行 # 响应体
response = """HTTP/1.1 200 OK
Content-Type:text/html

hello world
"""

c.send(response.encode())


c.close()
s.close()