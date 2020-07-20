from multiprocessing import *
from time import sleep
# fun函数在3秒内执行2次
def fun(name):
    print(name,"开始执行函数")
    sleep(2)
    print(name,"进程函数执行完了")

p = Process(target=fun,args=("进程执行",))
p.daemon=True
p.start()  # 执行了一次fun函数
fun("运行文件时候执行")   # 又执行了一次函数
p.join()
