import csv
import time


from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

# @cache_page(50)
from django.views.decorators.csrf import csrf_exempt


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