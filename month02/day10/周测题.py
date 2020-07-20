"""
1. 给你一个 n*m 的二维数组，每个元素保证递增，
每列元素保证递增，
试问如何找到某个数字，或者判断这个数字不存在。
"""
num = 1
list01 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def get_number(num):
    for r in list01:
        for c in r:
            if num < c:
                print("不存在")
                return
            elif num == c:
                print("存在")
                return
    else:
        print("不存在")

get_number(num)

# 给你一个长度为n的数组，其中只有一个数字出现了1次，其他均出现2次，问如何快速的找到这个数字。
# list02 = [1,1,5,8,8,7,7,9,9,6,5]
# for number in list02:
#     if list02.count(number) ==1:
#         print(number)
