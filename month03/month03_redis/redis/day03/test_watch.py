import redis
from time import sleep

pool = redis.ConnectionPool(host='127.0.0.1', db=1, port=6379, password='123456')
r = redis.Redis(connection_pool=pool)


def double_count(user_id):
    key = 'account_%s' % user_id
    with r.pipeline(transaction=True) as pipe:
        while True:
            try:
                # 监控键key的值是否发生改变
                pipe.watch(key)
                # 获取key的值
                # 　需要提前在１库里面里面set有account_tedu这个key
                value = int(r.get(key))
                value *= 2
                print('newvalue:', value)
                # 为了给在客户端修改key的值留点时间 睡眠20秒
                print('sleep is start------')
                sleep(20)
                print('sleep is over------')
                # 开始事务
                pipe.multi()
                pipe.set(key, value)
                # 　执行事务
                pipe.execute()
                break  # 别人没改 就会走到这里
            except redis.WatchError:
                print('value 在事务期间 被修改')
                continue

    return int(r.get(key))


if __name__ == '__main__':
    print(double_count('tedu'))
