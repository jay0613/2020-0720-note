from socket import socket

s = socket()
s.bind(("0.0.0.0",8888))
s.listen(5)


while True:
    connfd,sddr = s.accept()
    data = connfd.recv(4096).decode()
    if not data:
        break

    result_line = data.split("\n")[0]
    info = result_line.split(" ")[1]
    if info == "/":
        with open("index.html") as f:
            msga = f.read()
        msg = """http/1.1 200 ok
        Content-Type: text/html
        Content-Length:109\r\n
        
        %s
        """%msga

        connfd.send(msg.encode())