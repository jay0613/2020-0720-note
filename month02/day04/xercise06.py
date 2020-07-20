import re
s = "Alex:1998,Sunny:1997"
pattern = r"(\w+):(?P<year>\d+)"  # 这是小写w
l = re.finditer(pattern,s)
for i in l:   # 每个i代表匹配到的一个位置
    print(i.group("year"))  # 只获取年份