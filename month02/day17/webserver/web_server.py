"""
author: Bill
email: 240110075@qq.com
time: 2020-7-19
env: Python3.6
web_server exercise
把同学做的网页放到网上，让其他人也可以访问
"""

from socket import *
from select import *
import re


class WebServer:
    def __init__(self,host="0.0.0.0",post=80,html=None):
        self.host = host
        self.post = post
        self.html = html
        self.create_sock()
        self.bind()
        self.__rlist = []
        self.__wlist = []
        self.__xlist = []


    def create_sock(self):
        self.sock = socket()

    def bind(self):
        ADDR = (self.host,self.post)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind(ADDR)

    def start(self):
        self.sock.listen(5)
        print("Listen the port %d"%self.post)
        self.__rlist.append(self.sock)
        while True:
            rs,ws,xs = select(self.__rlist,self.__wlist,self.__xlist)
            for r in rs:
                if r is self.sock:
                    connfd,addr = r.accept()
                    self.__rlist.append(connfd)
                else:
                    try:
                        self.handle(r)
                    except:
                        self.__rlist.remove(r)
                        r.close()

    def handle(self, connfd):
        result = connfd.recv(1024).decode()
        pattern = "[A-Z]+\s/\S*"
        match = re.match(pattern,result)
        if match:
            data = match.group()
            self.send_response(connfd,data)
        else:
            connfd.close()
            self.__rlist.remove(connfd)

    def send_response(self, connfd, match):
        info = match.split(" ")[-1]
        if info == "/":
            filename = self.html + "/index.html"
            print(filename)
        else:
            filename = self.html + info

        try:
            f = open(filename,'rb')
        except:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type: text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry....</h1>"
            response = response.encode()
        else:
            data = f.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            response += "Content-Length:%d\r\n"%len(data)
            response += "\r\n"
            response = response.encode() + data
        finally:
            connfd.send(response)

if __name__ == '__main__':
    web = WebServer(host="0.0.0.0",post=8888,html="./static")
    web.start()

