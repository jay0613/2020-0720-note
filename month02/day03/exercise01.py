b1 = b"hello"

print(type(b1))
print(b1.decode())
b2 = "你好".encode()
print(b2)
b3 = "#".encode()
print(b3)

c1 = b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(c1.decode())