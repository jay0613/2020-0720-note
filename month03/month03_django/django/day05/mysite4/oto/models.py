from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)


class Wife(models.Model):
    name = models.CharField(max_length=20)
    # 外键
    author = models.OneToOneField(Author,on_delete=models.CASCADE)