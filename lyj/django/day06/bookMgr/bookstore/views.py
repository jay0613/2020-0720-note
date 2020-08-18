from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Book


# Create your views here.
def all_book(request):
    all_book = Book.objects.filter(is_active=True)
    return render(request,'bookstore/all_book.html',locals())


def add_book(request):
    if request.method=="GET":
        return render(request,'bookstore/add_book.html')
    elif request.method=="POST":
        title = request.POST['title']
        pub = request.POST['pub']
        price = request.POST['price']
        market_price = request.POST['market_price']
        try:
            Book.objects.create(title=title,pub=pub,price=price,market_price=market_price)
        except Exception as e:
            print('create error %s'%e)
            return HttpResponse('create book error')
        return HttpResponseRedirect('/bookstore/all_book')

def delete_book(request):
    bid = request.GET.get('bid')
    if not bid:
        return HttpResponse('--bid error--')
    try:
        book = Book.objects.get(id=bid,is_active=True)
    except Exception as e:
        print('error is %s'%e)
        return HttpResponse('get book error')
    book.is_active = False
    book.save()
    return HttpResponseRedirect('/bookstore/all_book')


def update_book(request,bid):
    try:
        book = Book.objects.get(id=bid, is_active=True)
    except Exception as e:
        return HttpResponse('get book error')

    if request.method =="GET":
        return render(request,'bookstore/update_book.html',locals())
    elif request.method=="POST":
        price = request.POST['price']
        market_price = request.POST['market_price']
        book.price = price
        book.market_price = market_price
        book.save()

        return HttpResponseRedirect('/bookstore/all_book')



