"""
消费者
"""

import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
while True:
    task = r.brpop('pylist1',10)
    # (b'pylist1', b'sendMail_123@tedu.cn_456@tedu.cn_hello')
    print(task)
    if task:
        task_data = task[1]
        # 'sendMail_123@tedu.cn_456@tedu.cn_hello'
        task_str = task_data.decode()
        # ['sendMail', '123@tedu.cn', '456@tedu.cn', 'hello']
        task_list = task_str.split('_')
        print('receive task ,task type is %s'%task_list[0])
        # if task is sendMail.call SendMail function
    else:
        print('no task!')
