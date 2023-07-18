from django.db import models


# Create your models here.

class Words_Bank(models.Model):
    word = models.CharField(max_length=250, default='', null=True, verbose_name='单词')

    pos = models.TextField(default='', null=True, verbose_name='词性')

    pt_us = models.CharField(max_length=250, default='', null=True, verbose_name='美式音标')

    pt_uk = models.CharField(max_length=250, default='', null=True, verbose_name='英式音标')

    pronunce_us = models.CharField(max_length=250, default='', null=True, verbose_name='美式发音')

    pronunce_uk = models.CharField(max_length=250, default='', null=True, verbose_name='英式发音')

    inflection = models.TextField(default='', null=True, verbose_name='变形式')

    sentence = models.TextField(default='', null=True, verbose_name='例句')


class European_Standard_Level(models.Model):
    word = models.CharField(max_length=250, default='', null=True, verbose_name='单词')

    guideword = models.CharField(max_length=250, default='', null=True)

    level = models.CharField(max_length=250, default='', null=True)

    part_of_speech = models.CharField(max_length=250, default='', null=True)

    topic = models.CharField(max_length=250, default='', null=True)

    tag = models.CharField(max_length=250, default='', null=True, verbose_name='来源')

# 形容词
# class Adjective(models.Model):
#     # 原词
#     word = models.CharField(max_length=50)

#     # 结构
#     pos = models.CharField(max_length=50)

#     comparative = models.CharField(max_length=150, default='', null=True)

#     superlative = models.CharField(max_length=150, default='', null=True)
#     # 等级
#     # grade = models.CharField(max_length=50)


# # 副词
# class Adverb(models.Model):
#     # 原词
#     word = models.CharField(max_length=50)

#     # 结构
#     pos = models.CharField(max_length=50)

#     comparative = models.CharField(max_length=150, default='', null=True)

#     superlative = models.CharField(max_length=150, default='', null=True)

#     # 等级
#     # grade = models.CharField(max_length=50)


# # 介词
# class Prep(models.Model):
#     # 原词
#     word = models.CharField(max_length=50)

#     # 结构
#     pos = models.CharField(max_length=50)


# # 名词
# class Moun(models.Model):
#     #     名词复数
#     words = models.CharField(max_length=50)

#     # 原词
#     word = models.CharField(max_length=50)

#     # 结构
#     pos = models.CharField(max_length=50)

#     # 等级
#     # grade = models.CharField(max_length=50)


# # 非动词
# class Nonverbpos(models.Model):
#     # 原词
#     word = models.CharField(max_length=50)

#     # 结构
#     pos = models.CharField(max_length=50)


# # 量词数据库
# class Quantifierlemma(models.Model):
#     # 原词
#     word = models.CharField(max_length=50)


# # 动词单性
# class Verbpluspos(models.Model):
#     # 原词
#     word = models.CharField(max_length=50)

#     pos = models.CharField(max_length=50)

#     _pos = models.CharField(max_length=50)

#     vbz = models.CharField(max_length=50)

#     vbg = models.CharField(max_length=50)

#     vbd = models.CharField(max_length=50)

#     vbn = models.CharField(max_length=50)

#     # 等级
#     # grade = models.CharField(max_length=50)


# # 动词多性
# class Verbpluspos_Double(models.Model):
#     # 原词
#     word = models.CharField(max_length=50)

#     pos = models.CharField(max_length=50)

#     _pos = models.CharField(max_length=50)

#     vbz = models.CharField(max_length=50)

#     vbg = models.CharField(max_length=50)

#     vbd = models.CharField(max_length=50)

#     vbn = models.CharField(max_length=50)

#     # 等级
#     # grade = models.CharField(max_length=50)


# # 代词
# class Pronoun(models.Model):
#     # 原词
#     word = models.CharField(max_length=50)

#     # 结构
#     pos = models.CharField(max_length=50)

#     # 类型
#     type = models.CharField(max_length=50)


# # 固定搭配
# class fixedMatch(models.Model):
#     # 搭配词组
#     text = models.CharField(max_length=150)

#     vbd = models.CharField(max_length=50)

#     vbg = models.CharField(max_length=50)

#     vbn = models.CharField(max_length=50)

#     vbz = models.CharField(max_length=50)


# # 领域
# class Categorydict(models.Model):
#     # 原词
#     word = models.CharField(max_length=150)

#     pos = models.CharField(max_length=50)

#     # 1：人称；2：职业;3:人物
#     type = models.CharField(max_length=50)

#     # 领域词复数
#     words = models.CharField(max_length=150)


# # 状语固定搭配
# class Adverbial_fixation(models.Model):
#     # 原词
#     word = models.CharField(max_length=150)

#     meaning = models.CharField(max_length=100)


# # 序数词
# class Ordinal_Numeral(models.Model):
#     cardinal = models.CharField(max_length=150)

#     ordinal = models.CharField(max_length=150)
