# -*- coding=utf-8 -*-
import pymysql

# with open('ldh.jpg', 'rb',encoding="UTF-8") as f:
#     data = f.read()

f = open('ldh.jpg', 'rb')
data = f.read()

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8',
                     use_unicode=True
                     )
cur = db.cursor()

try:
    sql = 'update class set image=%s where id = 7;'% pymysql.Binary(data)
    cur.execute(sql)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()