f = open("file.txt","w")
n = f.write("hello")
print("写入了%d个字节"%n)

l = ["哈喽","你好"]
f.writelines(l)