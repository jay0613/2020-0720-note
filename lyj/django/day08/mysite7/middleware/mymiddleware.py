from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re


class MyMW(MiddlewareMixin):
    # urls主路由前检查
    def process_request(self, request):
        print("中间件1方法 process_request 被调用")

    # views视图前检查
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件1方法 process_view 被调用")

    # 返回相应给浏览器前的检查
    def process_response(self, request, response):
        print("中间件1方法 process_response 被调用")
        return response


class MyMW2(MiddlewareMixin):
    # urls主路由前检查
    def process_request(self, request):
        print("中间件1MyMW2方法 process_request 被调用")

    # views视图前检查
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件1MyMW2方法 process_view 被调用")

    # 返回相应给浏览器前的检查
    def process_response(self, request, response):
        print("中间件1MyMW2方法 process_response 被调用")
        return response


class VisitLimit(MiddlewareMixin):
    # 该字典记录某ip的访问次数，地址为键,访问次数为值
    visit_times = {}

    # urls主路由前检查
    def process_request(self, request):
        cip = request.META['REMOTE_ADDR']
        if not re.match(r'^/test', request.path_info):
            return None
        # 获取这个cip在字典中对应的值，如果这个cip还没访问过则，把0返回给times
        times = self.visit_times.get(cip, 0)
        if times >= 5:
            return HttpResponse('no way!')
        self.visit_times[cip] = times + 1
        print('%s visitme %d times' % (cip, times + 1))
