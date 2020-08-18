from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Book

# Create your views here.
def all_book(request):
    all_book = Book.objects.filter(is_active=True)
    return render(request,'bookstore/all_book.html',locals())


def delete_book(request):
    bid = request.GET.get('bid')
    if not bid:
        return HttpResponse('--bid is error--')
    try:
        book = Book.objects.get(id=bid,is_active=True)
    except Exception as e:
        print("--no book!--%s"%e)
        return HttpResponse('---book is error----')
    book.is_active = False
    book.save()
    # 302跳转　
    return HttpResponseRedirect('/bookstore/all_book')


def update_book(request,bid):
    try:
        book = Book.objects.get(id=bid,is_active=True)
    except Exception as e:
        print("no this book,%s" % e)
        return HttpResponse("no this book")

    if request.method == "GET":
        return render(request,'bookstore/update_book.html',locals())
    elif request.method == "POST":
        price = request.POST.get('price')
        market_price = request.POST['market_price']
        book.price = price
        book.market_price = market_price
        book.save()
        # 302跳转　　　HttpResponseRedirect　主要做临时重定向作用
        return HttpResponseRedirect('/bookstore/all_book')
