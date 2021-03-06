# Generated by Django 2.2.13 on 2020-08-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_auto_20200810_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=18, verbose_name='年龄'),
        ),
    ]
