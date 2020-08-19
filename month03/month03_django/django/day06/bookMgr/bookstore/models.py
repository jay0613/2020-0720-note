from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField("书名", max_length=20)
    pub = models.CharField('出版社',max_length=20)
    price = models.DecimalField('定价',max_digits=5,decimal_places=2)
    market_price = models.DecimalField('零售价',max_digits=5,decimal_places=2)
    is_active = models.BooleanField('是否活跃',default=True)
