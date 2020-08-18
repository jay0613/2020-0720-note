import csv
import os
import time

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from test_upload.models import Content







# @cache_page(50)
def test_cache(request):
    # 1. 模拟生成页面是耗时的（复杂计算和复杂查询）
    # time.sleep(3)
    # 2. 如果时间变了，表示我没有使用缓存
    # t1 = time.time()
    # return HttpResponse('t1 is %s'%t1)
    return HttpResponse('访问这个路由也可以执行中间件函数')


def test_mw(request):
    print('--view do--')
    return HttpResponse('--test mw--')


@csrf_exempt
def test_csrf(request):
    if request.method == "GET":
        return render(request, 'test_csrf.html')
    elif request.method == "POST":
        username = request.POST['username']
        return HttpResponse('username is %s' % username)


def test_page(request):
    list1 = ['a', 'b', 'c', 'd', 'e']
    paginator = Paginator(list1,2)   # 把list1显示在页面中　　每页显示２个元素
    cur_page = request.GET.get('page',1)   # 返回页码,没有找到则返回１
    page = paginator.page(cur_page)     # 返回第cur_page页的信息
    return render(request,'test_page.html',locals())

# 下载
def test_csv(request):
    resp = HttpResponse(content_type='text/csv')
    # filename为保存时候的文件名
    resp['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    writer = csv.writer(resp)
    writer.writerow(['id', 'title','author'])
    writer.writerow([1,'python','张凯'])
    writer.writerow([2,'c++','马志国'])
    writer.writerow([3,'Django','佳欣'])
    return resp


@csrf_exempt
def test_upload(request):
    if request.method == "GET":
        return render(request,'test_upload.html')
    elif request.method == "POST":
        title = request.POST['title']
        a_file = request.FILES['myfile']

        #　方案１
        # 为了防止重名，可以在用户上传的文件后增加时间戳
        # # 创建文件保存的绝对路径
        # filename = os.path.join(settings.MEDIA_ROOT,a_file.name)
        # with open(filename, 'wb') as f:
        #     # a_file.file 文件的字节流数据
        #     data = a_file.file.read()
        #     f.write(data)
        # return HttpResponse("接收文件:" + a_file.name + "成功")

        # 方案２(推荐)   # 会把路径保存到数据库的test_upload_content表
        # 上传文件遇到重名的话会自动生成后缀，不会覆盖原文件
        # 保存的文件路径去数据库的同时，上传文件到MEDIA_ROOT+myfile路径下（models.py里面设置的）
        Content.objects.create(desc=title, myfile=a_file)
        return HttpResponse('----upload is ok-----')