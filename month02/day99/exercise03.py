
# 1.求出当前时间距离第二天0点0时0分的时间差，并在页面中显示相差的时间（15分）
import time

while True:
    now_hour = time.localtime()[3]
    now_min = time.localtime()[4]
    now_sec = time.localtime()[5]
    time.sleep(1)
    sec_sum = 24 *3600
    now_sec_sum = now_hour * 3600 + now_min *60 +now_sec
    differ_sec = sec_sum - now_sec_sum
    hour = differ_sec // 3600
    min = differ_sec % 3600 // 60
    sec = differ_sec % 3600 % 60
    print("距离明天还有 %02d:%02d:%02d "%(hour,min,sec))

# 2.编写程序求1到10的和并输出该结果?（10分）

# 3.编写程序找出以下数组中最大元素的下标位置及该元素的值?（15分）
