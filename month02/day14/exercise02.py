"""
thread1.py  线程基础使用
步骤： 1. 创建线程对象
      2. 启动线程
      3. 回收线程
"""

import threading
from time import sleep
import os

a = 1

# 线程函数
def music():
    global a
    print("a = ",a)
    a = 10000
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放: 葫芦娃")    # getpid()获取该进程的pid和29行获取的pid是同一个，因为是同一个进程



job = []
for i in range(4):  # 和上面创建的线程执行的任务同时运行
    # 线程对象
    t = threading.Thread(target=music)
    job.append(t)
    t.start()  # 启动线程

for j in job:
    j.join() # 回收线程

print("a:",a) # a==10000  #线程和进程不一样，前几天学的创建进程的那个内容a==1





