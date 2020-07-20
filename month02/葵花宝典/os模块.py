# os.path.isfile()和os.path.isdir() 分别检验给出的路径是一个目录还是文件 , 返回值True/False
# os.listdir(dirname):列出dirname下的目录和文件,返回值为文件列表
# os.getcwd():获得当前工作目录,以绝对路径格式显示
# os.curdir:返回当前目录（'.'）
# os.chdir(dirname):改变工作目录到dirname,可通过os.getcwd()查询
# os.path.isdir(name):判断name是不是目录,返回值True/False
# os.path.isfile(name):判断name这个文件是否存在,返回值True/False(只能判断文件)
# os.path.exists(name):判断是否存在文件或目录name,返回值True/False(可用于判断文件/目录)
# os.path.getsize(name):或得文件大小，如果name是目录返回0L(自测返回4096)
# os.mkdir("file")　　创建目录
# os.rename("oldname","newname")  重命名文件（目录）.文件或目录都是使用这条命令
# shutil.copyfile("oldfile","newfile")　　复制文件:oldfile和newfile都只能是文件
# shutil.copy("oldfile","newfile")  oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
# shutil.copytree("olddir","newdir")  复制文件夹.olddir和newdir都只能是目录，且newdir必须不存在
# shutil.move("oldpos","newpos")  移动文件（目录）
# os.remove(file):删除一个文件
# os.rmdir("dir")  只能删除空目录
# shutil.rmtree("dir")  空目录、有内容的目录都可以删
# os.path.getmtime(path): 文件或文件夹的最后修改时间，从新纪元到访问时的秒数。
# os.path.getatime(path): 文件或文件夹的最后访问时间，从新纪元到访问时的秒数。
# os.path.getctime(path): 文件或文件夹的创建时间，从新纪元到访问时的秒数。
