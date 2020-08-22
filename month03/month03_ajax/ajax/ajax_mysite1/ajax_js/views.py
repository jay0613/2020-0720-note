from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def test_xhr(request):
    return render(request,'ajax_js/test_xhr.html')


def test_get(request):
    return render(request,'ajax_js/test_get.html')


def test_jq_get(request):
    return render(request,'ajax_js/test_jq_get.html')


def xhr_get_server(request):
    return HttpResponse('hello Ajax from server')


def test_json(request):
    return render(request,'ajax_js/test_json.html')