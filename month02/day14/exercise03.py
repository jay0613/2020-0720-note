"""
thread_attr.py
线程属性示例
"""
from threading import Thread
from time import sleep
def fun():
    sleep(3)
    print("线程属性示例")
t = Thread(target = fun,name = "Tarena")    # 这行也可以定义线程名称
t.setDaemon(True) # 主线程退出分支线程也退出  # 所以11行的“线程属性示例”这几个字不会打印

t.start()
t.setName("Tedu")  # 设置线程名称
print("Name:",t.getName()) # getName获取线程名称
print("is alive:",t.is_alive()) # 是否在生命周期  # 返回True或者false
print("Daemon:",t.isDaemon())  # isDaemon查看daemon属性值，因为15行设置了True，所以此处返回True
t.join()