# Generated by Django 2.2.13 on 2020-08-10 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20200810_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=18, max_length=10, verbose_name='年龄'),
        ),
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
    ]