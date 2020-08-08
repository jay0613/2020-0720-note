from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Django--")

def page1(request):
    return HttpResponse("--this is first page1--")

def page2(request):
    return HttpResponse("--this is first page2--")


def pagen(request,num):
    return HttpResponse("这是第%s个页面"%num)


def mymath(request,a,op,b):
    if op not in ["add","sub","mul"]:
        return HttpResponse("输入有误")
    if op == "add":
        request =a +b
    elif op == "sub":
        request = a-b
    else:
        request = a * b
    return HttpResponse("结果是：%s"%request)


def birthday(request,year,month,day):
    result = ("生日为：%s年%s月%s日"%(year,month,day))
    return HttpResponse(result)


def score1(request,name,a,b,c):
    average = (int(a)+int(b)+int(c))/3
    total = int(a)+int(b)+int(c)
    result = ("%s-平均分：%s-总分：%s"%(name,average,total))
    return HttpResponse(result)


