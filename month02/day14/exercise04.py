from threading import Thread,Lock
from time import sleep

a = b = 0
lock = Lock()

def func():
    while True:
        lock.acquire()
        if a == b:
            print("a+b=",a+b)
        else:
            print("哈哈")
        # sleep(3)
        lock.release()


t = Thread(target=func)
t.start()


while True:
    with lock:
        a += 1
        b += 1
        print(a)
t.join()





