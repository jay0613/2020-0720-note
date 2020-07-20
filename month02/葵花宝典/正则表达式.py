import re
# 目标字符串
s = "Alex:1994,Sunny:1999"
pattern = r"(\w+):(\d+)" # 正则表达式

p2 = r':'
l1 = re.findall(p2,'s')
print(l1)

l1 = re.findall('ab',"ababcdefabcd")
print(l1) # ['ab', 'ab', 'ab']
l2 = re.findall('com|cn',"www.baidu.com/www.tmooc.cn")
print(l2) # ['com', 'cn']
l3 = re.findall('张.丰',"张三丰,张四丰,张五丰")  # 元字符：.  # 匹配规则：匹配除换行外的任意一个字符，例如 张\n丰 就不行
print(l3) # ['张三丰', '张四丰', '张五丰']
l4 = re.findall('[aeiou@#]',"How are # you!@") # 表示 [] 中的任意一个字符  # 匹配字符集中的任意一个字符
print(l4) # ['o', 'a', 'e', '#', 'o', 'u', '@']  #注意：没有i
l5 = re.findall('[aeiou]',"hello world") # 表示 [] 中的任意一个字符  # 匹配字符集中的任意一个字符
print(l5) # ['e', 'o', 'o']
l9 = re.findall('[^aeiou]',"hello world") # 元字符：[^字符集] # 匹配规则：匹配除了字符集以外的任意一个字符
print(l9) # ['h', 'l', 'l', ' ', 'w', 'r', 'l', 'd']
l6 = re.findall('[0-5]',"196532") # 表示[0-5]里区间内的任意一个字符
print(l6) # ['1', '5', '3', '2']
l7 = re.findall('[a-z]',"196hH532") # 表示[a-z]里区间内的任意一个字符  # 注意：大写区间表达[A-Z]
print(l7) # ['h'] # 注意：没有大写的H
l8 = re.findall('[0-9a-z]',"po@rt#18") # 区间可以混合书写
print(l8) # ['p', 'o', 'r', 't', '1', '8']
l8 = re.findall('[a-zA-Z]',"How are you？") # 区间可以混合书写
print(l8) # ['H', 'o', 'w', 'a', 'r', 'e', 'y', 'o', 'u']
l10 = re.findall('[^0-9]',"Use 007 port")  # 元字符：[^字符集]   # 匹配规则：匹配除了字符集以外的任意一个字符
print(l10) # ['U', 's', 'e', ' ', ' ', 'p', 'o', 'r', 't']


l10 = re.findall('[^张].',"张三李四") # [^张]会取“三李四”的第一个"三"，“.”会取一下个字符“李”
print(l10)  # ['三李']
l11 = re.findall('^Jame',"Jame，hello") # 元字符: ^  匹配规则：匹配目标字符串的开头位置  当Jame是字符串的开头位置的时候才可以匹配成功 如果是l11 = re.findall（'^Jame',"hello,Jame"）则不会匹配成功，下一行打印就会为空
print(l11) # ['Jame']
l12 = re.findall('jie$',"hi,jie") # 元字符: $  匹配规则: 匹配目标字符串的结尾位置  和上一行元字符^类似
print(l12) # ['jie']
l13 = re.findall('^jie$',"jie")  # 规则技巧: ^ 和 $必然出现在正则表达式的开头和结尾处。如果两者同时出现，则中间的部分必须匹配整个目标字符串的全部内容。
print(l13) # ['jie']
l14 = re.findall('wo*',"wooooo~~w!") # 元字符: *  匹配规则：匹配前面的字符出现0次或者多次  # *只会作用于他前面的一个字符o,不会作用于w
print(l14) # ['wooooo', 'w']   # 对比一下上面l1更容易理解
l14 = re.findall('[a-zA-Z]*',"How#are#you") # 用字符集和*同时使用时候匹配不上的会返回空字符，在末尾也会返回空字符
print(l14) # ['How', '', 'are', '', 'you', '']
l14 = re.findall('[A-Z][a-z]*',"How are you? Find Jame") # 匹配大写开头的单词  # *只作用于[a-z]  # 匹配大写字母开头加上若干个小写字母组合的单词
print(l14) # ['How', 'Find', 'Jame']
l15 =  re.findall('[A-Z][a-z]+',"Hello World I am Good") # 元字符：+  # 匹配规则： 匹配前面的字符出现1次或多次
print(l15) # ['Hello', 'World', 'Good']  # 注意此处没有返回I 因为用“+”之后，大写后面最少要连一个小写

# 元字符：?  # 匹配规则： 匹配前面的字符出现0次或1次
l16 = re.findall('-?[0-9]+',"Jame,age:18, -26") # 元字符：?  # 匹配规则： 匹配前面的字符出现0次或1次  # ?只会作用于他前面一个字符- 原理和*差不多，只是次数不一样
print(l16) # ['18', '-26']
l16 = re.findall('[^ ]+',"Port-9 Error #404# %@STD") # 除了空格以外的字符，一个或多个
print(l16) # ['Port-9', 'Error', '#404#', '%@STD']
l17 = re.findall('1[0-9]{10}',"Jame:13886495728") # 元字符：{n}  # 匹配规则： 匹配前面的字符出现n次
print(l17) # ['13886495728']
l18 = re.findall('[1-9][0-9]{5,10}',"Baron:1259296994") # 元字符：{m,n}  # 匹配规则： 匹配前面的字符出现m-n次
print(l18) # ['1259296994']

l19 = re.findall('\d{1,4}',"Mysql: 3306, http:80") # 元字符： \d \D  # 匹配规则：\d 匹配任意数字，和[0-9]一个意思， # \D 匹配任意非数字字符，和[^0-9]一个意思  # {1,4} 一位到四位数字
print(l19) # ['3306', '80']
l20 = re.findall('\w+',"server_port = 8888") # 元字符： \w \W  # 匹配规则: \w 匹配普通字符，\W 匹配非普通字符   # 说明: 普通字符指数字，字母，下划线，汉字(日文等等也可以)，UTF-8都行。
print(l20) # ['server_port', '8888']
l21 = re.findall('\w+\s+\w+',"hello world") # 元字符： \s \S   # 匹配规则: \s 匹配空字符，\S 匹配非空字符   # 说明：空字符指 空格 \r \n \t \v \f 字符
print(l21) # ['hello world']

# 元字符： \A \Z  匹配规则： \A 表示开头位置,和^一样功能。 \Z 表示结尾位置,和$一样功能
l11 = re.findall('\AJame',"Jame，hello")
print(l11) # ['Jame']
l12 = re.findall('jie\Z',"hi,jie")
print(l12) # ['jie']

# 元字符： \b \B
l22 = re.findall(r'\bis\b',"This is a test.") # 元字符： \b \B   # 匹配规则： \b 表示单词边界，\B 表示非单词边界  # 说明：单词边界指数字字母下划线(包括汉字)与其他字符的交界位置。# \w与其他字符的交界位置
print(l22) # ['is']  # 上一行的r表示转变成原生字符串  # r'\bis\b' 等同于 '\\bis\\b'  # 第一条\是python的转义  # r的使用请看下面几行的注释

# 正则表达式的转义
l23 = re.findall('-?\d+\.?\d*',"123,-123,1.23,-1.23") #  匹配特殊字符 . 时使用 \. 表示本身含义   #特殊字符:  . * + ? ^ $ [] () {} | \
print(l23) # ['123', '-123', '1.23', '-1.23']
print("hi \n jie")  # \n具有换行功能，所以打印不在同一行
print(r"hi \n jie") # 前面加了r，此时\n没有换行功能 # hi \n jie

"""
# r的转义：在编程语言中，常使用原生字符串书写正则表达式避免多重转义的麻烦。
python字符串 --> 正则 --> 目标字符串
"\\$\\d+" 解析为 \$\d+ 匹配 "$100"  # 第一个\是python语言的转义符，第二个\是正则表达式语言的转义符，
也就是说前面l19-l23的带\的代码，为了避免多重转义麻烦都应该多加一个\
但是还有一种更方便的写法，就是在前面加个r
"\\$\\d+" 等同于 r"\$\d+"

"""

"""
贪婪模式和非贪婪模式
1. 定义
贪婪模式: 默认情况下，匹配重复的元字符总是尽可能多的向后匹配内容。比如: * + ? {m,n}
非贪婪模式(懒惰模式): 让匹配重复的元字符尽可能少的向后匹配内容。
2. 贪婪模式转换为非贪婪模式
在匹配重复元字符后加 '?' 号即可
* : *?
+ : +?
? : ??
{m,n} : {m,n}?
"""
l24 = re.findall('ab*?',"abbbbbbbb") # 非贪婪模式下，*b最少是取0个b
print(l24) # ['a']
l24 = re.findall(r'\(.+?\)',"(abcd)efgh(higk)")  # “（”和“）”是特殊字符所以前面要加\转义  # 此处的?是转换为非贪婪模式
print(l24) # ['(abcd)', '(higk)']  # 贪婪模式下会打印(abcd)efgh(higk)  因为abcd)efgh(higk都可以用.+匹配出来

print("-------------------------------------------------------------------------------")

# re调用函数
pattern1 = r"(\w+):(\d+)" # 正则表达式
l = re.findall(pattern1,s)  # 返回值: 匹配到的内容列表,如果正则表达式有子组则只能获取到子组对应的内容
print(l) # [('Alex', '1994'), ('Sunny', '1999')]
"""
regex = compile(pattern,flags = 0)
功能: 生产正则表达式对象
参数:
    pattern 正则表达式
    flags 功能标志位,扩展正则表达式的匹配
返回值: 正则表达式对象
"""
# regex表达式对象调用函数  # 上面一行有注释
regex = re.compile(pattern,flags=0)
l = regex.findall(s,) # 逗号后面不写就是默认截取整个目标字符串s作为匹配目标
print(l) # [('Alex', '1994'), ('Sunny', '1999')]

"""
regex.findall(string,pos,endpos)
功能: 根据正则表达式匹配目标字符串内容
参数:
    string 目标字符串
    pos 截取目标字符串的开始匹配位置
    endpos 截取目标字符串的结束匹配位置
返回值: 匹配到的内容列表,如果正则表达式有子组则只能获取到子组对应的内容
"""
regex = re.compile(pattern,flags=0)
l = regex.findall(s,0,14)  # 在Alex:1994,Sunn这14个字符里匹配pattern
print(l)  # [('Alex', '1994')]
print("分割线444444444444444")

"""
re.split(pattern,string,flags = 0)
功能: 使用正则表达式匹配内容,切割目标字符串
参数:
    pattern 正则表达式
    string 目标字符串
    flags 功能标志位,扩展正则表达式的匹配
返回值: 切割后的内容列表
"""
# 按照正则表达式的内容,切割目标字符串
l = re.split(r'[,:]',s)  # 遇到:或者遇到,就切割   # 切割s
print(l) # ['Alex', '1994', 'Sunny', '1999']


"""
re.sub(pattern,replace,string,max,flags = 0)
功能: 使用一个字符串替换正则表达式匹配到的内容
参数:
    pattern 正则表达式
    replace 替换的字符串
    string 目标字符串
    max 最多替换几处,默认替换全部
    flags 功能标志位,扩展正则表达式的匹配
返回值: 替换后的字符串
"""
s = re.sub(r':','-',s) # 在s中把匹配到的所有:替换成-
print(s) # Alex-1994,Sunny-1999

"""
re.subn(pattern,replace,string,max,flags = 0)
功能: 使用一个字符串替换正则表达式匹配到的内容
参数:
    pattern 正则表达式
    replace 替换的字符串
    string 目标字符串
    max 最多替换几处,默认替换全部
    flags 功能标志位,扩展正则表达式的匹配
返回值: 替换后的字符串和替换了几处
"""
# 使用字符串替换匹配到的部分
s = re.subn(r':','-',s,1)
print(s) # ('Alex-1994,Sunny:1999', 1)


