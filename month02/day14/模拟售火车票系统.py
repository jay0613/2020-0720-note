from threading import Thread
from time import sleep

list01 = []
for i in range(1,501):
    str0 = "T"+str(i)
    list01.append(str0)


def maipiao(str):
    while True:
        if not list01:
            print(str,"票卖完了")
            return
        else:
            print(str, "----", list01[0])
            del list01[0]
            sleep(0.1)

job = []
for i in range(1,11):
    str0 = "w"+str(i)
    t = Thread(target=maipiao,args=(str0,))
    job.append(t)
    t.start()

for i in job:
    i.join()