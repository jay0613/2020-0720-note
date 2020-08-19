from django.contrib import admin

# Register your models here.

from .models import *


class AuthorManage(admin.ModelAdmin):
    list_display = ['id', 'name']


class WifeManage(admin.ModelAdmin):
    list_display = ['id', 'name', 'author']


admin.site.register(Author, AuthorManage)
admin.site.register(Wife, WifeManage)
