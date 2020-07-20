from socket import *
from select import select

tcp_sock = socket()
tcp_sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)  # 端口重用
tcp_sock.bind(("0.0.0.0",8888))
tcp_sock.listen(5)

rlist = [tcp_sock]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is tcp_sock:
            connfd,addr = r.accept()
            print("connect from",addr)
            rlist.append(connfd)
        else:
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            wlist.append(r)
    for w in wlist:
        w.send(b"serverOK")
        wlist.remove(w)

    for x in xlist:
        pass