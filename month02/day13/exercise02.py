from multiprocessing import Process

#自定义类
class Myprocess(Process):
    def __init__(self,val):
        self.val = val
        super().__init__()   # 加载父类属性

    def run1(self):
        print("执行run1方法,参数：",self.val)

    def run2(self):
        print("执行run2方法,参数：",self.val)

    def run(self):
        self.run1()
        self.run2()

mp = Myprocess(2)
mp.start()
mp.join()