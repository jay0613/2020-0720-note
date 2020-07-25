"""
这两个模块都是操作文件的
"""
import os
import shutil

dirname = "/home/tarena/note/month02"
bool = os.path.isfile(dirname)         # 检验该 文件 是否存在, 返回值True/False(可用于判断文件)
# bool = os.path.isdir(dirname)         # 检验该 文件夹 是否存在 , 返回值True/False(可用于判断目录)
# bool = os.path.exists(dirname)        # 判断是否存在该文件或目录,返回值True/False(可用于判断文件/目录)
list01 = os.listdir(dirname)          # 列出dirname下的目录和文件,返回值为文件列表
str1 = os.getcwd()                     # 获得当前工作目录,以绝对路径格式显示
# str1 = os.curdir                      # 返回当前目录,不过返回的是一个点 “.”
os.chdir(dirname)                     # 改变工作目录到dirname,可通过os.getcwd()查询
number = os.path.getsize(dirname)     # 或得文件字节数大小，如果name是目录返回0L(自测返回4096)
os.mkdir("/home/tarena/note/month05") # 创建目录
os.rename("oldname","newname")         # 重命名文件（目录）.文件或目录都是使用这条命令
shutil.copyfile("oldfile","newfile")  # 复制文件:oldfile和newfile都只能是文件（都必须是绝对路径）
shutil.copy("oldfile","newfile")      # oldfile只能是文件，newfile可以是文件(会重命名)，也可以是目标目录(都必须写绝对路径)
shutil.copytree("olddir","newdir")    # 复制文件夹.olddir和newdir都只能是目录，且newdir必须不存在
shutil.move("oldpos","newpos")         # 移动文件（目录）
os.remove("file")                       # 删除一个文件
os.rmdir("dir")                        # 只能删除空的目录
shutil.rmtree("dir")                   # 空目录、有内容的目录都可以删
mktime1 = os.path.getmtime(dirname)        # 返回文件或文件夹的最后修改时间(时间戳)，从新纪元到访问时的秒数。
# mktime1 = os.path.getatime(dirname)     # 文件或文件夹的最后访问时间(时间戳)，从新纪元到访问时的秒数。
# mktime1 = os.path.getctime(dirname)        # 文件或文件夹的创建时间(时间戳)，从新纪元到访问时的秒数。

# 整理完毕 其他都是没啥用
