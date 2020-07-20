"""
pool.py
进程池 使用实例
"""

from multiprocessing import Pool
from time import sleep,ctime

# 进程池事件  #必须写在创建进程池的前面
def worker(msg):
    sleep(2)
    print(ctime(),'--',msg)

# 创建进程池
pool = Pool(4) #参数代表创建多少个进程，不写的话就是系统默认的创建多少个进程

# 向进程池队列中添加事件
for i in range(10):
    msg = "Tedu %d"%i
    pool.apply_async(func=worker,args=(msg,))  # 将事件加入进程池队列执行

# 关闭进程池
pool.close()

# 回收进程池
pool.join()
