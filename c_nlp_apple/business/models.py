from django.db import models


# Create your models here.


class Save_Word(models.Model):
    word = models.CharField(max_length=250, default='', null=True, verbose_name='单词')

    create_date = models.DateField(auto_now=True, verbose_name='创建日期')
