from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Note


# Create your views here.


def login_check(fn):
    def wrap(request, *args, **kwargs):
        # 　如果session 没有数据
        if 'username' not in request.session or 'uid' not in request.session:
            # 检查 cookies　有没有数据
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:  # 如果cookies也没有数据 则让用户跳到登录页面
                return HttpResponseRedirect('/user/login')
            else:
                # 回写session
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)
    return wrap


@login_check
def add_view(request):
    if request.method == "GET":
        return render(request, 'note/add_note.html')
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        uid = request.session['uid']
        Note.objects.create(title=title, content=content, user_id=uid)
        # 找到这个id用户写的所有所有笔记
        note = Note.objects.filter(user_id=uid)
        return render(request,'note/show_title.html',locals())


def show_content(request):
    title = request.GET.get('title')
    print("+++++++",title)
    # 获取该条笔记的id
    uid = request.GET.get('uid')
    note = Note.objects.filter(title=title,id=uid)[0]
    print("-------------",title,uid,note)
    return render(request,'note/show_content.html',locals())


def delete(request):
    # note2为该id用户发布的所有笔记
    nid = request.GET.get('nid')
    try:
        note1 = Note.objects.get(id=nid)
        user_id = note1.user_id
        note1.delete()
        note = Note.objects.filter(user_id=user_id)
    except:
        print("删除失败")
    return render(request,'note/show_title.html',locals())