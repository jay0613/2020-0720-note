from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# action 表单提交给谁　　　　method 提交方式
HTML_DATA = """
    <form method='get' action='/test_get_post?a=100&b=200'>
        用户名:<input type='text' name='username'>
        密码:<input type='password' name='password'>
        <input type='submit' value='提交'>
    </form>
"""


def test_get_post(request):
    if request.method == "GET":
        # 只能拿到一个ａ的值，拿到的最后一个ａ的值
        # print(request.GET["a"])
        # 拿到多个a的值
        # print(request.GET.getlist('a'))
        # print(request.GET["b"])
        # print(request.GET["c"])
        print(request.GET.get('c', "100"))  # 试探性拿值即使没拿到也不会报错　# 100为默认值　　没拿到ｃ　返回１００
        print(request.path_info)
        print(request.get_full_path())
        return HttpResponse(HTML_DATA)
    elif request.method == "POST":
        username = request.POST["password"]
        a = request.GET.get("a")
        b = request.GET.get("b")
        return HttpResponse("欢迎%s,%s,%s" % (username, a, b))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        return "姓名:%s,年龄:%s"%(self.name,self.age)

def hello():
    return "hello world"


def test_html(request):
    t = loader.get_template("test_html.html")
    dict1 = {}
    dict1["name"] = 'wangwu'
    dict1['age'] = 18
    # dict1['hobby'] = ['吃饭','睡觉','打豆豆']
    dict1['hobby'] = []
    dict1["scores"] = {"语文":100,"数学":120,"英语":95}
    dict1['person'] = Person("张飞",35)
    dict1['func1'] = hello
    dict1["script"] = '<script>alert("这是一个弹框")</script>'
    html = t.render(dict1)
    return HttpResponse(html)


def test_cal(request):
    if request.method == "GET":
        # t = loader.get_template('test_cal.html')
        # html = t.render()
        # return HttpResponse(html)
        return render(request,'test_cal.html')
    elif request.method == "POST":
        # t = loader.get_template('test_cal.html')
        x = request.POST['x']
        y = request.POST['y']
        if not x or not y:
            return HttpResponse("请输入一个数值")
        try:
            x = int(x)
            y = int(y)
        except Exception as e:
            print("error is %s" % e)
            return HttpResponse("请输入一个数值")

        op = request.POST["op"]
        result = 0
        if op == "add":
            result = x+y
        elif op == "sub":
            result = x-y
        elif op == "mul":
            result = x * y
        elif op == "div":
            result = x / y
        # dict1 = {}
        # dict1['x'] = x
        # dict1['y'] = y
        # dict1['result'] = result
        # dict1['op'] = op
        # return render(request, 'test_cal.html',dict1)
        return render(request, 'test_cal.html',locals())


