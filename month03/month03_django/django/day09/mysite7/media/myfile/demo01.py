"""
    while 的 else
    猜数字2.0
        最多猜三次
        正确提示:恭喜你才对了
        超过次数提示:游戏失败

"""
import random

random_number = random.randint(1, 100)
print(random_number)
count = 1
while count <= 3:
    get_number = int(input("请输入要猜的数字（1-100）："))
    if get_number == random_number:
        print("恭喜你才对了,总共猜了" + str(count) + "次")
        break
    elif get_number > random_number:
        print("大了")
    else:
        print("小了")

    count += 1
else: # if count > 3
    # while 条件不满足才执行else语句
    # while 循环从break结束,不执行else语句
    print("游戏失败")
