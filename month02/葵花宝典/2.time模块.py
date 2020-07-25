import time
import datetime
# 1. 获取当前时间元组
# 时间元组: 年/月/日/时/分/秒/星期/一年的第几天/夏令时
# (tm_year=2020, tm_mon=7, tm_mday=11, tm_hour=9, tm_min=30, tm_sec=40, tm_wday=5, tm_yday=193, tm_isdst=0)
tuple_time1 = time.localtime()

# 2. 获取当前时间戳
# 时间戳: 从1970年1月1日 0时0分0秒到现在经过的秒数
mktime1 = time.time()  # 1592377581.6000147

# 3. 时间戳 --> 时间元组
# (tm_year=2020, tm_mon=7, tm_mday=11, tm_hour=9, tm_min=30, tm_sec=40, tm_wday=5, tm_yday=193, tm_isdst=0)
tuple_time2 = time.localtime(1592377581.6000147)

# 4. 时间元组 --> 时间戳
mktime2 = time.mktime(tuple_time2)  # 1592377581.0

# 5. 时间元组 --> 字符串
# 语法:字符串 = time.strftime(格式,时间元组)
str_time1 = time.strftime("%y/%m/%d %H:%M:%S", tuple_time2)  # 20/06/17 15:06:21
str_time2 = time.strftime("%Y/%m/%d %H:%M:%S", tuple_time2)  # 2020/06/17 15:06:21
str_time4 = time.asctime(tuple_time2)  # Wed Jun 17 15:06:21 2020

# 6. 字符串 --> 时间元组
# 语法:时间元组 = time.strptime(时间字符串,格式)
# (tm_year=2020, tm_mon=6, tm_mday=17, tm_hour=15, tm_min=6, tm_sec=21, tm_wday=2, tm_yday=169, tm_isdst=-1)
tuple_time3 = time.strptime("2020/06/17 15:06:21", "%Y/%m/%d %H:%M:%S")

# 7. 获取当前时间
str_time3 = time.ctime()  # Tue Jun 30 09:31:48 2020  # Sat Jul 11 09:30:40 2020

# 8. 睡眠
# time.sleep(2)  # 运行到该行会暂停2秒再往后执行
# 整理完毕 其他都是没啥用的


# 9. 返回本地当前时间 datetime格式
datetime = datetime.datetime.today()   # 2020-07-24 21:53:11.173582
print(datetime)
print(type(datetime))
