from django.contrib import admin
from .models import Book,Author
# Register your models here.

class BookManage(admin.ModelAdmin):
    # 显示哪些字段
    list_display = [ 'title', 'pub', 'price', 'market_price']
    # 哪些可以点击进入编辑框
    list_display_links = ['title','pub']
    # 搜索哪个字段
    search_fields = ['title','pub']
    # 一进页面就可以改
    list_editable = ['market_price']
    #　过滤器,显示在右侧
    list_filter = ['pub','price']

admin.site.register(Book, BookManage)


class AuthorManage(admin.ModelAdmin):
    # 显示哪些字段
    list_display = [ 'id','name', 'age']
    # 哪些可以点击进入编辑框
    list_display_links = ['name']
    # 搜索哪个字段
    search_fields = ['name','age']
    # 一进页面就可以改
    list_editable = ['age']
    #　过滤器,显示在右侧
    list_filter = ['name','age']

admin.site.register(Author, AuthorManage)





