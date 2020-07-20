from multiprocessing import Process
import os
size = os.path.getsize("dict.txt")
f = open("dict.txt","r")

def func1():
    f1 = open("h3.txt", "w")
    while True:
        data = f.readline()
        if os.path.getsize("h3.txt") > size//2:
            break
        f1.write(data)

def func2():
    f2 = open("h4.txt", "w")
    while True:
        f2.seek(size//2,0)



p = Process(target=func1)
p.start()

# func()
p.join()