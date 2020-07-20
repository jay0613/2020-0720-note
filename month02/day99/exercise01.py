import time
while True:
    print("listen",end="")
    for i in range(3):
        print(".",end="",flush=True)
        time.sleep(0.5)
        if i == 2:
            print("")

# list01 = [1,2,3,4,5]
# print("a","b",end="",sep="+")