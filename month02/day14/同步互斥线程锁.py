"""
thread_lock.py
线程锁演示
"""

from threading import Thread,Lock
from time import sleep

a = b = 0
lock = Lock() # 锁对象

def value():
    while True:
        lock.acquire()   #上锁 # 如果lock已经上锁再调用acquire会阻塞   # witn lock也可以上锁，witn代码块结束自动解锁
        if a == b:
            print('a = %d,b = %d'%(a,b))
        lock.release() # 解锁操作

t = Thread(target=value)
t.start()
sleep(1)
while True:
    with lock:  # with上锁
        a += 1
        b += 1
                # with语句块结束自动解锁
t.join()

