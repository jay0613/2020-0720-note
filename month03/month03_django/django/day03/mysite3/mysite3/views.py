from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def test_html(request):
    name = "奥斯特洛夫斯基"
    age = 15
    return render(request,'test_html.html',locals())


def base(request):

    return render(request,'base.html')


def news(request):
    return render(request,'news.html')


def sport(request):
    print(reverse("pgnurl", args=[300]))    # /page/300   刷新网页在终端打印
    return render(request,'sport.html')

def pagen(request,num):
    return HttpResponse("page %s"%num)


def test_static(request):
    return render(request,'test_static.html')