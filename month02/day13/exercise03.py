from multiprocessing import Process
import time

#
# def estimate_prime_number(number):
#     for i in range(2,number):
#         if number % i == 0:
#             return False
#     return True
#
# def get_prime(begin,end):
#     list01 = []
#     for number in range(begin,end+1):
#         if estimate_prime_number(number):
#             list01.append(number)
#     print(list01)
#
# old_time = time.time()
# get_prime(1,100000)
# time1 = time.time()-old_time
# print("用时：",time1)

def estimate_prime_number(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def get_prime(begin,end):
    list01 = []
    for number in range(begin,end+1):
        if estimate_prime_number(number):
            list01.append(number)
    print(sum(list01))


p = Process(target=get_prime,args=(1,25000))
old_time = time.time()
p.start()
p.join()
time1 = time.time()-old_time
print("用时：",time1)