import os
print(os.path.getsize("./test.txt"))  # 5

print(os.listdir("."))   # ['exercise01.py', 'test.txt']

print(os.path.exists("./test.txt"))  # True

print(os.path.isfile("./test.txt"))  # True

os.remove("./test.txt")



