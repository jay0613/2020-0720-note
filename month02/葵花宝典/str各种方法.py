string = "h\teLLo,worlD!"
str0 = "  刘-德-华  "
dict01={'name':'小明','class':'201903','score':597.5}
str09 = "asd123こんにちは李一杰"
string20 = "**a*"
str20 = "AAAA!!"
str21 = "asd123こんにちは李一杰"
string21 = "一0"
intab = "aeiou"
outtab = "12345"
str2 = "this is string example....wow!!!"
list01 = ["a","b","c"]
# str01 = string.capitalize()  # 把字符串的第一个字符大写,其余字符全变小写,并返回该新的字符串
# str02 = string.center(20)  # 返回一个原字符串居中,并使用空格填充至长度20的新字符串
# str03 = "+".join(list01)  # 刘+德+华  # 遍历参数里面的列表或者字符串把里面每个字符用"+"拼接成新字符串并返回
# number01 = string.count("l")  # 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
# list02 = str0.split("-",1)  # 以"-"为分隔符分割str0,分割成2份,并存入列表返回该列表
# list02 =  str0.rsplit("-",1)  # 类似于 split() 方法，只不过该方法是从字符串最后面开始搜索分隔符开始分割。
# b = string.find("L")   # 检测 L 是否存在在 string 中，如果存在则返回该字符的索引值(只会返回一个)，否则返回-1
# a = string.rfind("L")  # 类似于 find()函数，不过是从右往左开始查找，找到第一个返回索引值.
# a1 = string.index("L")  # 跟find()方法一样，只不过如果str不在 string中会报一个异常.
# a = string.rindex("L")  # 类似于 index()，不过是从右边开始.如果该字符不在 string中会报一个异常.
# a2 =  string.upper() # 把字符串的所有小写字母转换成大写,并返回新字符串
# a2 =  string.swapcase()  # 将字符串中大写转换为小写，小写转换为大写,并返回新字符串
# a2 = string.lower()   # 把字符串的所有大写字母转换成小写,并返回新字符串，仅对"A-Z有效"
# a3 = string.casefold()  # 把字符串的所有大写转换成小写,并返回新字符串,对其他国家语言也有效（例如：#德语的"ß"正确的小写是"ss"）
# # 两者的区别是：lower() 方法只对ASCII编码，也就是‘A-Z’有效，对于其他语言（非汉语或英文）中把大写转换为小写的情况只能用 casefold() 方法。
# a4 = string.endswith("!")  # 如果string是以"!"结尾的话,返回True,否则返回false,如果beg 和 end 指定值，则在指定范围内检查。
# a4 = string.startswith("h") #  如果string是以"h"开头的话,返回True,否则返回false,如果beg 和 end 指定值，则在指定范围内检查。
# a5 = string.title()  # Hello,World! # 返回新的string,每个单词首字母都是大写，其余字母均为小写
# bool = str0.istitle()  # 如果每个单词首字母都是大写，其余字母均为小写则返回 True，否则返回 False
# a6 = string.encode()  # 把string转换成字节码形式
# a7 = a6.decode()   # 把字节码转换成字符串
# a8 = string.expandtabs()  # 如果string中含有\t符号，会把\t转换成空格，并返回转换后的新字符串，
# a9 = str0.strip()  # 去除两侧空格
# b1 = "我是{},{},{}{}".format("杰",2,1,"哈哈")  # 把"杰",2,1,"哈哈"放到前面字符串的括号内,然后返回给b1
# s1='{class}班{name}总分：{score}'.format_map(dict01)  # format_map参数只能传入字典等映射关系的数据 # 返回值给s1
# b2 = str09.isalnum()  # 如果所有字符都是字母或数字或国家文字则返回 True,否则返回 False  #注意不能包含下划线“_”
# bool = string21.isalpha() # 如果字符串所有字符都是字母则返回 True, 否则返回 False
# bool = string21.isdecimal() # 检查字符串是否只包含正整数字符，如果是返回 true，否则返回 false。数字0也返回false
# bool = string21.isdigit() # 如果字符串只包含阿拉伯数字则返回 True 否则返回 False..
# bool = string21.isnumeric()  # 如果字符串中只包含数字字符(所有国家数字都行)，则返回 True，否则返回 False
# bool = str21.isidentifier()  # 判断该字符串是否是标识符，或者说是否可以用作变量名，如果是返回True 否则返回false
# bool = string20.islower()  # 判断字符串中是否有大写字母，如果有则返回false，没有则返回True
# bool = str20.isupper()  # 判断字符串中是否有小写字母，如果有则返回false，没有则返回True
# bool = str20.isprintable()  # 判断字符串是否可全部打印出来，可以则返回True,否则返回false,   内含\r,\n,\t,\b等等这些转义字符是打印不出来的
# bool = string20.isspace()  # 如果字符串中只包含空白，则返回 True，否则返回 False.   字符串为空时返回false
# str1 = string20.ljust(5, "*")  # 返回一个原字符串左对齐,并使用 * 填充至长度 5 的新字符串，填充的字符默认为空格。
# str1 =  string20.rjust(5, "*")  # 返回一个原字符串右对齐,并使用* 填充至长度 5 的新字符串，填充的字符默认为空格。
# str1 = string20.zfill(10)  # 返回一个原字符串右对齐，并使用数字0 填充至长度 10 的新字符串，填充的字符必须是数字0
# str1 = string20.lstrip("*")  # 删除字符串左边的指定字符,默认是删除空格。
# str1 = string20.rstrip("*")  # 删除字符串末尾的指定字符，默认是删除空格.
# str1 = str2.replace("is","AA",2) #把str2中的"is" 替换成"AA"，返回新字符串，参数2表示最多替换2次，不写默认全部替换。
# trantab = str.maketrans(intab,outtab) # 制作返回翻译表，第一个参数里面的每个字符和第二个参数的每个参数一一对应，必须和下面的translate方法配合使用。两个参数都是字符串，且长度一致。
# str1 = str2.translate(trantab)  # 使用翻译表，把str2里面对应字母替换成对应的数字
# print(str1)  # th3s 3s str3ng 2x1mpl2....w4w!!!
# str1 = str2.partition(" ")  #返回一个固定包含3个元素的元组，参数为分隔符，第一个元素为分隔符左边的字符串，第二个为分隔符本身，第三个为分隔符右边的字符串。
# str1 = str2.rpartition(" ")  #类似于上面partition方法，只是该方法是从目标字符串的末尾也就是右边开始搜索分割符,而partition是从左开始搜索。
# list01 =  string20.splitlines()  # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，参数默认为 False，返回的值删掉换行符，如果为 True，则保留换行符。
# print('ab c\n\nde fg\rkl\r\n'.splitlines(True))  # ['ab c\n', '\n', 'de fg\r', 'kl\r\n']

#整理完毕




