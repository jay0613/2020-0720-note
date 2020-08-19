from django.http import HttpResponse


def set_cookies(request):
    resp = HttpResponse('--set cookies is ok!--')
    resp.set_cookie('uuname', 'tarena', 10)
    return resp


def get_cookies(request):
    print(request.COOKIES.get('uuname', 'no value'))
    return HttpResponse('--set cookies is ok!--')


def delete_cookies(request):
    resp = HttpResponse('--delete cookies is ok!--')
    resp.delete_cookie('uuname')
    return resp


def set_session(request):
    request.session['uname']='tarena'
    return HttpResponse('--set session--')


def get_session(request):
    value = request.session.get('uname','no value')
    return HttpResponse('session value is %s'%value)