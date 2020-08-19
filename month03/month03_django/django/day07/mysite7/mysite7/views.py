import time

from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(50)
def test_cache(request):
    # 1. 模拟生成页面是耗时的（复杂计算和复杂查询）
    time.sleep(3)
    # 2. 如果时间变了，表示我没有使用缓存
    t1 = time.time()
    return HttpResponse('t1 is %s'%t1)
