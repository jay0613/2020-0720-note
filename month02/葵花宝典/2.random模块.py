import random
list01 = [1,5,9,3,5,7]
number = random.randint(1, 3)  # 生成1-3随机整数包括1和3
number = random.random()   # 生成一个0到1的小数  # 0.8365611962287474
number = random.uniform(3,1)  # 生成1-3随机小数 # 小的参数也可以放在第一个参数
number = random.randrange(10,30,2)  # 相当于从range(10, 30, 2)中获取一个随机数
number = random.choice(list01)  # 从序列中获取一个随机元素
random.shuffle(list01)  # 将一个列表中的元素顺序打乱
list02 = random.sample(list01,3) # 从指定序列中随机获取指定长度的片断并随机排列

# 整理完毕