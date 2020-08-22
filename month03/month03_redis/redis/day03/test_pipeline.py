# 创建连接池并连接到redis
import redis
from time import time

pool = redis.ConnectionPool(host='127.0.0.1', db=0, port=6379, password='123456')
r = redis.Redis(connection_pool=pool)


def withpipeline(r):  # 使用流水线,1000个命令一次通信
    p = r.pipeline()
    for i in range(1000):
        key = 'test1' + str(i)
        value = i + 1
        p.set(key, value)
    p.execute()


def withoutpipeline(r):  # 不使用流水线,1000个命令1000次通信
    for i in range(1000):
        key = 'test2' + str(i)
        value = i + 1
        r.set(key, value)


if __name__ == '__main__':
    t1 = time()
    withoutpipeline(r)
    t2 = time()
    print('没有使用流水线 时间消耗: %s'%(t2-t1))

    t3 = time()
    withpipeline(r)
    t4 = time()
    print('使用流水线 时间消耗: %s'%(t4-t3))
