from socket import *
from select import select

s = socket()
s.bind(("0.0.0.0",8888))
s.listen(5)
