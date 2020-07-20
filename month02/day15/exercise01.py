"""
    打印大写字母A-Z
    # for i in range(65,91):
#     print(chr(i))
"""

from threading import Thread,Lock
lock2 = Lock()
lock1 = Lock()


def func1():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i+1)
        lock2.release()
def func2():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

t1 = Thread(target=func1)
t2 = Thread(target=func2)
lock2.acquire()

t1.start()
t2.start()
t2.join()
t1.join()




