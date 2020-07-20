"""
编写一个函数，参数传入一个设备端口名称
         返回值是这个端口描述中所对应的 address
         信息

         思路： 根据端口名确定段落
               再从段落中匹配目标

         提示： 段与段之间有空行
               每段第一个单词是端口名称
               端口名称可能很复杂
"""

import re

# 获取每个段落
def get_info():
    f = open("log.txt")

    while True:
        info = ""
        for line in f:
            if line == "\n":
                # 这是一个空行
                break
            info += line
        # 结束死循环
        if not info:
            break
        yield info

    f.close()
    return

def get_address(port):
    for data in get_info():
        # 从一段中获取首单词  data
        obj = re.match(r"\S+",data)
        if port == obj.group():
            # 是这一段 开始匹配
            pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            result = re.search(pattern,data)
            if result:
                return result.group()
            else:
                return "Unknown"
    return "port error"





print(get_address("MgmtEth0/RSP0/CPU0/0"))