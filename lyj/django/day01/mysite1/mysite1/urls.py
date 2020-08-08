"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    # 127.0.0.1:8000/index
    path("index",views.index),
    # 127.0.0.1:8000/page/1
    path("page/1", views.page1),
    # 在浏览器输入这个路径127.0.0.1:8000/page/2　　则会调用views.page2
    path("page/2", views.page2),
    # 127.0.0.1:8000/page/55
    path("page/<int:num>",views.pagen),
    # http://127.0.0.1:8000/page/10/add/5
    path("page/<int:a>/<str:op>/<int:b>",views.mymath),
    # year和month和day是关键字传参　　所以必须和views.py里的birthday方法形参名一致
    re_path(r'^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$',views.birthday),
    re_path(r'^birthday/(?P<day>\d{1,2})/(?P<month>\d{1,2})/(?P<year>\d{4})$',views.birthday),
    # 返回分数
    # path("<str:name>/<int:a>/<int:b>/<int:c>",views.score1),
    re_path(r'^(?P<name>\w+)/(?P<a>\d{1,3})/(?P<b>\d{1,3})/(?P<c>\d{1,3})$',views.score1),
]
