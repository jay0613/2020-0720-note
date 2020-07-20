from threading import Thread
from socket import *
import os,time

ADDR = ("0.0.0.0",8888)

dir = "/home/tarena/month02/葵花宝典/"

class FTPServer(Thread):
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd


    def run(self):
        while True:
            data = self.connfd.recv(128).decode()
            if data == "LIST":
                self.do_list()

            elif data[:4] == "RETR":
                filename = data.split(' ')[-1]
                self.do_get(filename)

            elif data[:4] == "STOR":
                filename = data.split(" ")[-1]
                self.do_put(filename)

    def do_get(self,filename):
        try:
            f = open(dir+filename,"rb")
        except:
            self.connfd.send("FAIL".encode())
            return
        else:
            self.connfd.send("OK".encode())
            time.sleep(0.1)
            while True:
                data = f.read(128)
                if not data:
                    time.sleep(0.1)
                    self.connfd.send("##".encode())
                    break
                self.connfd.send(data)
            f.close()
    def do_list(self):
        file_list = os.listdir(dir)
        if not file_list:
            self.connfd.send(b"FAIL")
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
            file = "\n".join(file_list)
            self.connfd.send(file.encode())

    def do_put(self, filename):
        file_list = os.listdir(dir)
        if filename in file_list:
            self.connfd.send(b"FAIL")
            return
        else:
            self.connfd.send(b"OK")
            result = self.connfd.recv(128)
            if result != b"NO":
                f = open(dir+filename,"wb")
                while True:
                    data = self.connfd.recv(1024)
                    if data == b"##":
                        break
                    f.write(data)
                f.close()
            else:
                return


def main():
    s = socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen()
    print("Listen the port 8888")
    while True:
        try:
            connfd,addr = s.accept()
            print("connect from",addr)
        except KeyboardInterrupt:
            s.close()
            return
        t = FTPServer(connfd)
        t.setDaemon(True)
        t.start()

if __name__ == '__main__':
    main()