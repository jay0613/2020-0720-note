import re

s = "Alex:1998,Sunny:1997"
pattern = r"\w+:\d+"
l = re.findall(pattern,s)
print(l)  # ['Alex:1998', 'Sunny:1997']

s = "Alex:1998,Sunny:1997"
# 因为有子组，只获取子组的内容
pattern = r"(\w+):\d+"
l = re.findall(pattern,s)
print(l)  # ['Alex', 'Sunny']