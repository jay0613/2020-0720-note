"""
练习3： 在一个文件 my.log 中不间断的写入如下内容
1. 2020-01-01  14:15:16
2. 2020-01-01  14:15:18
3. 2020-01-01  14:15:20
4. 2020-01-01  14:15:22
5. 2020-01-01  14:15:24
6. 2020-01-01  14:17:29
7. 2020-01-01  14:17:31
 每个时间占一行，每隔2秒写入一行
 当程序终止以后，下次启动，要求序号能够衔接继续写
 写的内容每写入一行就要在文件中显示
"""
# import time
# f = open("my.log","a+")
# count = 1
# f.seek(0,0)
# if f.read() != "":
#     f.seek(0, 0)
#     number = f.readlines()[-1].strip(".")[0]
#     count = int(number)+1
# while True:
#     tuple_time = time.localtime()
#     time01 = time.strftime("%Y-%m-%d  %H:%M:%S\n",tuple_time)
#     data = str(count)+". "+time01
#     f.seek(0,2)
#     f.write(data)
#     f.flush()
#     count += 1
#     time.sleep(3)


import time
f = open("my.log","r+")
count = 1
if f.read() != "":
    f.seek(0, 0)
    number = f.readlines()[-1].strip(".")[0]
    count = int(number)+1
while True:
    tuple_time = time.localtime()
    time01 = time.strftime("%Y-%m-%d  %H:%M:%S\n",tuple_time)
    data = str(count)+". "+time01
    f.seek(0,2)
    f.write(data)
    f.flush()
    count += 1
    time.sleep(3)

