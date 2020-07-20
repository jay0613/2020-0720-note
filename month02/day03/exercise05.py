with open("file.txt","rb+") as f:
    data = f.read(10)
    f.seek(10,0)
    f.write(b"liyijie")