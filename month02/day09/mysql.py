import pymysql
import re
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")

cur = db.cursor()
name = input("请输入姓名：")
sql = "select * from class where name=%s"

cur.execute(sql,[name])
row = cur.fetchone()
print(row)

cur.close()
db.close()