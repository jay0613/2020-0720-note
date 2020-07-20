from socket import socket
ADDR = ("127.0.0.1",8888)
tcp_socket = socket()
tcp_socket.connect(ADDR)

f = open("刘德华.jpg","rb")

while True:
    ldh = f.readline()
    print(ldh)
    if not ldh:
        print("发送完成")
        break
    else:
        tcp_socket.send(ldh)

tcp_socket.close()