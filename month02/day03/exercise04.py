f1 = open("ldh.jpg", "rb")
f2 = open("dh.jpg", "wb")
while True:
    data = f1.read(1024)
    if data == b"":
        break
    f2.write(data)
    print(data)

f1.close()
f2.close()