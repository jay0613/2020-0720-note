import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
# r.hset('h2', 'uname', 'tedu')
# print(r.hget('h2', 'uname'))  # b'tedu'
# # 设置多个字段值时候，第二个参数是一个字典
# r.hmset('h2', {'age': 22, 'desc': 'it edu'})
# print(r.hgetall('h2'))  # {b'uname': b'tedu', b'age': b'22', b'desc': b'it edu'}
# print(r.hkeys('h2'))  # [b'uname', b'age', b'desc']
# print(r.hvals('h2'))  # [b'tedu', b'22', b'it edu']


# 2 对set的操作
# r.sadd('user_1','peiqi','qiaozhi','danni')
# r.sadd('user_2','peiqi','qiaozhi','lingyang')
# # 交集
# print(r.sinter('user_1', 'user_2'))   # {b'peiqi', b'qiaozhi'}

# 3. 对sortedset的操作
r.zadd('z11',{'mazhiguo':1000,'wangweichao':2000,'tedu':1500})
# 找z11里面的所有元素,withscores=True表示把分值也返回
# [(b'mazhiguo', 1000.0), (b'tedu', 1500.0), (b'wangweichao', 2000.0)]
print(r.zrange('z11', 0, -1, withscores=True))  # 顺序排名
print(r.zrevrange('z11', 0, -1, withscores=True))  # 逆序排名
print(r.zcard('z11'))  # 3  # z11中的元素个数
r.zadd('z22',{'tedu':1000})
# 结果保存在z33   # 'z11','z22'参与运算  # sum  求和
print(r.zinterstore('z33', ('z11', 'z22'), aggregate='sum'))
print(r.zrange('z33', 0, -1, withscores=True)) # [(b'tedu', 2500.0)]
