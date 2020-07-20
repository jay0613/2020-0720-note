from socket import *
from time import sleep

ADDR = ("124.70.187.114",8888)

dir = "/home/tarena/month02/day15/ftp/"
class FTPClient():
    def __init__(self,s):
        super().__init__()
        self.s = s
    def do_list(self):
        self.s.send("LIST".encode())
        data = self.s.recv(128).decode()
        if data =="OK":
            file = self.s.recv(1024).decode()
            print(file)
        else:
            print("文件库为空！")

    def do_get(self,filename):
        data = "RETR "+filename
        self.s.send(data.encode())
        result = self.s.recv(128)
        if result.decode() == "OK":
            f = open(dir + filename, "wb")
            while True:
                data = self.s.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()
        else:
            print("文件不存在！")

    def do_put(self, filename):
        data = "STOR "+filename
        self.s.send(data.encode())
        result = self.s.recv(1024)
        if result == b"OK":
            try:
                f = open(dir+filename,"rb")
            except:
                print("该文件不存在！")
                self.s.send(b"NO")
                return
            else:
                while True:
                    data = f.read(1024)
                    if not data:
                        sleep(0.1)
                        self.s.send(b"##")
                        break
                    self.s.send(data)
                f.close()
        else:
            print("文件已存在！")


def main():
    s = socket(AF_INET,SOCK_STREAM)
    s.connect(ADDR)
    t = FTPClient(s)
    while True:
        print("============ 命令选项==============")
        print("***           list           ***")
        print("***         get  file        ***")
        print("***         put  file        ***")
        print("***           exit           ***")
        print("==================================")
        cmd = input("请输入命令：")
        if cmd == "list":
            t.do_list()
        elif cmd[:3] == "get":
            filename = cmd.split(" ")[-1]
            t.do_get(filename)
        elif cmd[:3] == "put":
            filename = cmd.split(" ")[-1]
            t.do_put(filename)



if __name__ == '__main__':
    main()