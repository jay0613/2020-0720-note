import re
s = "Alex:1998,Sunny:1997"
l = re.sub(r"\W+","#",s)  # 这是大写W
print(l) # Alex#1998#Sunny#1997