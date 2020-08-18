import redis


r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
key_list = r.keys('*')  # 找到0库的所有键
print(key_list)
# 通用命令
print(r.exists('li'))   # 1 表示li列表存在
print(r.exists('l5'))   # 0 表示l5列表不存在
# 字符串类型
r.set('name1','liyijie',100) # 设置键ｎａｍｅ1　值liyijie　　过期时间１００秒
print(r.get('name1'))  # liyijie
# 列表类型
r.lpush('l2','a','b','c''d')
print(r.lrange('l2', 0, -1))
r.ltrim('l2',0,1)
print(r.lrange('l2', 0, -1))
