"""
练习2：
通过input输入一个目录（目录中有很多文件可能有文件夹），
删除这个目录中所有大小小于10字节的普通文件
"""
import os
# path01 = input("输入目录:")

list_dir = os.listdir("../day99")
for file in list_dir:
    if os.path.isfile("../day99"+"/"+file) and os.path.getsize("../day99"+"/"+file) <= 10:
            os.remove("../day99"+"/"+file)
            print("删除成功",file)


