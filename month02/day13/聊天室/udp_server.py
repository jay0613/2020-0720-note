from socket import *
from multiprocessing import Process


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

ADDR = ("0.0.0.0",8888)
sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(ADDR)
user = []
def recv():
    while True:
        data, addr = sockfd.recvfrom(1024)
        print(data.decode())
        if data.decode() == "##":
            break
        for person in user:
            sockfd.sendto(data, person[1])


p = Process(target=recv)

while True:
    data,addr = sockfd.recvfrom(1024)
    number = data.decode()
    if number[-2:] == "##":
        for person in user:
            if number == person[0]:
                data = "o"
                sockfd.sendto(data.encode(),addr)
        user.append((number, addr))
        data = "ok"
        sockfd.sendto(data.encode(), addr)

    else:
        for person in user:
            if number == person[0]+"##":
                data = "ok"
                sockfd.sendto(data.encode(),addr)



p.start()
