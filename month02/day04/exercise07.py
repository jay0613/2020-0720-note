import re
s = "Alex:1998,Sunny:1997"
pattern = r"\w+"  # 这是小写w
l = re.match(pattern,s)
print(l.group())
