import re

# s = "13713788072"
# pattern = '1[35789]\d{9}'
# res = re.findall(pattern, s)
# print(res)
#
#
# s = "this is book"
# pattern = r'this is book'
# res = re.findall(pattern, s)
# print(res)


s = "<a><b>nihao</b></a>"
pattern = r'<(?P<key1>.+)><(?P<key2>.+)>.*</(?P=key2)></(?P=key1)>'
res = re.search(pattern, s)
print(res.group())


