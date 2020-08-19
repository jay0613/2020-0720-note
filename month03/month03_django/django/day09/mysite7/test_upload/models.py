from django.db import models

# Create your models here.

# 数据库的表test_upload_content只保存文件路径，真正的文件保存在MEDIA_ROOT+myfile路径下
class Content(models.Model):
    desc = models.CharField(max_length=100)
    # MEDIA_ROOT+myfile    在MEDIA_ROOT路径下再拼接myfile路径
    myfile = models.FileField(upload_to='myfile')