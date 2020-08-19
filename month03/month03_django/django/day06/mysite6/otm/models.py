from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=20,unique=True)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)