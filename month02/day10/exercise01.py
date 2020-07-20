import pymysql
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

cur = db.cursor()
f = open("dict.txt", "r")
list01 = []
for line in f:
    # word = [line.split(" ")[0],line.split(" ",2)[-1].strip()]
    a = line.split(" ")[0]
    b = line.split(" ",2)[-1].strip()
    list01.append((a,b))
    if line == "":
        break
try:
    sql1 = "insert into words(word,mean) values (%s,%s);"
    cur.executemany(sql1,list01)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()


cur.close()
db.close()







