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
list01 = [
    (29,'张飞',25,'m',75,'蜀'),
    (30,'张三',26,'m',75,'蜀'),
    (31,'张四',20,'m',75,'蜀'),
]
try:
    sql = "select * from class where name='%s'"%name
    # sql1 = "insert into class values(%s,%s,%s,%s,%s,%s)"
    # cur.execute(sql,[name])
    cur.execute(sql)
    # cur.executemany(sql1,list01)
    print(cur.fetchone())
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
cur.close()
db.close()