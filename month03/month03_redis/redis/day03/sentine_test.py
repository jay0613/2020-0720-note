from redis.sentinel import Sentinel

#生成哨兵连接
sentinel = Sentinel([('localhost', 26379)], socket_timeout=0.1)
#生成多个哨兵
# sentinel = Sentinel([('localhost', 26379),('localhost', 26380)], socket_timeout=0.1)


#初始化master连接
master = sentinel.master_for('tedu', socket_timeout=0.1, db=1)
slave1 = sentinel.slave_for('tedu',socket_timeout=0.1, db=1)
slave2 = sentinel.slave_for('tedu',socket_timeout=0.1, db=1)

#使用redis相关命令
master.set('mymaster', 'yes')
master.set('mymaster2', 'yes5555')
print(slave1.get('mymaster'))  # b'yes'
print(slave2.get('mymaster2'))   # b'yes5555'