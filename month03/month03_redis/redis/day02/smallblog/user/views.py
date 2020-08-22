from django.http import HttpResponse
from django.shortcuts import render
import redis
from .models import User

# Create your views here.

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

def detail_view(request, user_id):
    # 首先检查缓存中是否有数据.
    cache_key = 'user:%s'%user_id
    # 判断该key是否存在,刚运行的时候没有该key，下面生成的
    if r.exists(cache_key):
        #　获取这条数据的所有属性和对应的值，返回字典类型
        data = r.hgetall(cache_key) # {key1:value1,key2:value2}
        # {'username':'tedu','age':'18'}
        new_data = {k.decode():v.decode() for k,v in data.items()}
        username = new_data['username']
        age = new_data['age']
        html = 'cache:username is %s,age=%s'%(username,age)
        return HttpResponse(html)
    # 否则没有缓存，从mysql数据库中获取数据
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        return HttpResponse('no this user')
    html = 'username is %s,age=%s' % (user.username, user.age)
    # 将读取的数据保存到redis缓存
    r.hmset(cache_key,{'username':user.username,'age':user.age})
    # 设置过期时间
    r.expire(cache_key,60)
    return HttpResponse(html)


def user_update(request, user_id):
    # 获取传过来的age，没取到就给默认值１
    age = request.GET.get('age',1)
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        return HttpResponse('no this user')
    user.age = age
    user.save()
    # 更新或删除数据的时候都要删除一下缓存，避免缓存的数据和mysql里的不一致
    # 删除缓存
    cache_key = 'user:%s'%user_id
    r.delete(cache_key)
    return HttpResponse('update is ok')