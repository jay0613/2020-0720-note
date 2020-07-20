# 编程题
# 1. 给你一个长度为n的数组，其中只有一个数字出现大于n/2次，问如何快速找到这个数字（20分）

list01 = [2,2,2,2,2,5,6,4,5]
def get_number(list):
    for number in list:
        if list.count(number)> len(list)/2:
            return number

print(get_number(list01))


# 2.假设有100层的阶梯，给你两个完全一样的鸡蛋，请设计一种方法，能够试出从第几层阶梯开始往下仍鸡蛋鸡蛋会碎(30分)

# for i in range(1,101):






# 3.输入一个正数n，输出所有和为n 连续正数序列。（20分）
#     例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以输出3 个连续序列1-5、4-6 和7-8。

def get_count(n):
    a = 1
    list02 = []
    while True:
        num = 0
        list03 = []
        for number in range(a,n):
            list03.append(number)
            num += number
            if num > n:
                a += 1
                break
            elif num == n:
                list02.append(list03)
                a += 1
                break
            elif a == n-1:
                return list02

print(get_count(100))












