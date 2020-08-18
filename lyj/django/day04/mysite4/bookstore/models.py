from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(verbose_name="书名",max_length=50,unique=True)
    price = models.DecimalField('定价',max_digits=5,decimal_places=2)
    market_price = models.DecimalField('零售价',max_digits=5,decimal_places=2,default=0.0)
    pub = models.CharField("出版社",max_length=50,default='')
    is_active = models.BooleanField("是否活跃",default=True)
    def __str__(self):
        return "书名：%s,定价:%s,零售价：%s,出版社:%s,是否活跃:%s"%(self.title,self.price,self.market_price,self.pub,self.is_active)
    class Meta:
        # 默认的表名为app名+类名 太长 例如 bookstore_book
        db_table = 'book'  # 可改变当前模型类对应的表名


class Author(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=50,null=False)
    age = models.IntegerField(verbose_name="年龄",max_length=10,null=False,default=18)
    email = models.EmailField(verbose_name="邮箱",null=True)
    class Meta:
        db_table = "author"
        
    def __str__(self):
        return "%s-%s-%s"%(self.name,self.age,self.email)