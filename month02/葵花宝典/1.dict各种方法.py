dict1 = {"a": 1, "b": 2, "c": 1, "张三": 95, "李四": 100}
dict2 = {"张三": 3, "李四": 4, "王五": 5, "赵六": 6}

# dict01.clear()  # 清除字典内所有东西
a = dict1.copy()  # 复制字典
list01 = ["张三", "李四"]
# 创建一个新字典，以序列 list01 中元素做字典的键，5 为字典所有键对应的初始值
b = dict1.fromkeys(list01, 5)  # {'张三': 5, '李四': 5}
c = dict1.get("a",default=None)  # 1  返回指定键对应的值,如果指定键的值不存在时，返回该默认值。
dict1.setdefault("黎") # 和get()类似, 但如果键不存在于dict1字典中，将会添加键并将值设为default
d = dict1.values() # [1, 2, 1, 95, 100]  # 以列表返回字典中的所有值
f = dict1.keys() # ['a', 'b', 'c', '张三', '李四', '黎'] # 以列表返回字典所有的键
# dict1.clear() # 删除字典内所有元素
g = dict1.pop("张三")  #  删除该键,并返回该键对应的值
h = dict1.popitem()  # 删除字典中的最后一个键和值,并返回该键和值
dict1.update(dict2)  # 把字典dict2的键/值对更新到dict里

# items() 以列表返回可遍历的(键, 值) 元组数组  用for遍历拿到的是元组
j = dict1.items()  # [('a', 1), ('b', 2), ('c', 1), ('李四', 4), ('张三', 3), ('王五', 5), ('赵六', 6)]

# 整理完毕
