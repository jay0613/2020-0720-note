import re

s = """Hello
北京
"""
# l = re.findall(r"\w+",s)
# print(l)  # ['Hello', '北京']
l = re.findall(r"\w+$",s,flags=re.M)
print(l)  # ['Hello']


