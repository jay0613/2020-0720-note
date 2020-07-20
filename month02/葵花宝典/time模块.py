import time

# 1. 人类时间
# 时间元组: 年/月/日/时/分/秒/星期/一年的第几天/夏令时
print(time.localtime())  # time.struct_time(tm_year=2020, tm_mon=7, tm_mday=11, tm_hour=9, tm_min=30, tm_sec=40, tm_wday=5, tm_yday=193, tm_isdst=0)

# 2. 计算机时间
# 时间戳: 从1970年1月1日 0时0分0秒到现在经过的秒数
print(time.time())  # 1592377581.6000147

# 3. 时间戳 --> 时间元组
tuple_time = time.localtime(1592377581.6000147)

# 4. 时间元组 --> 时间戳
print(time.mktime(tuple_time))   # 1592377581.0

# 5. 时间元组 --> 字符串
# 语法:字符串 = time.strftime(格式,时间元组)
# 20/06/17 15:06:21
print(time.strftime("%y/%m/%d %H:%M:%S", tuple_time))   # 20/06/17 15:06:21
# 2020/06/17 15:06:21
print(time.strftime("%Y/%m/%d %H:%M:%S", tuple_time))   # 2020/06/17 15:06:21

# 6. 字符串 --> 时间元组
# 语法:时间元组 = time.strptime(时间字符串,格式)
print(time.strptime("2020/06/17 15:06:21", "%Y/%m/%d %H:%M:%S"))   # time.struct_time(tm_year=2020, tm_mon=6, tm_mday=17, tm_hour=15, tm_min=6, tm_sec=21, tm_wday=2, tm_yday=169, tm_isdst=-1)

# 7. 获取当前时间
print(time.ctime())  # Tue Jun 30 09:31:48 2020  # Sat Jul 11 09:30:40 2020
