"""
消息队列演示
注意： 消息存入与去除关系为 先入先出
"""
from multiprocessing import Queue,Process
from time import sleep
from random import randint
# 创建队列
q = Queue(5) # 最大存储5个消息
def request():
    for i in range(10):
        x = randint(1,100)
        y = randint(1,100)
        q.put((x,y))  # 写入消息队列   #put默认为阻塞函数（队列满了的时候会阻塞），可以设置隐藏参数block=false，则为非阻塞函数（如果设置非阻塞的话，队列满了也不会阻塞，造成结果是报错）put的另一个隐藏参数timeout，例如timeout=5则表示最多阻塞5秒（若设置put为非阻塞函数则不会用到timeout）
        print("=============")

def handle():
    while not q.empty():  #若q不是空的，则q.empty返回false，所以此处not false则是True，while只有在True的时候才执行
        data = q.get() # 读出消息队列   #get默认为阻塞函数（队列空了的时候会阻塞），可以设置隐藏参数block=false，则为非阻塞函数（如果设置非阻塞的话，队列空了也不会阻塞，造成结果是报错）put的另一个隐藏参数timeout，例如timeout=5则表示最多阻塞5秒（若设置put为非阻塞函数则不会用到timeout）
        print("x + y = ",data[0]+data[1])
        sleep(2)
p1 = Process(target=request)
sleep(1)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()