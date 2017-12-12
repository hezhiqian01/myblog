# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User

# Create your models here.



class Catagory(models.Model):
    name = models.CharField('名称', max_length=30)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('名称', max_length=16)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField('标题', max_length=32)
    author = models.ForeignKey(User, verbose_name='作者')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    content = models.TextField('博客内容')
    catagory = models.ForeignKey(Catagory, verbose_name='分类')
    tags = models.ManyToManyField(Tag,verbose_name='标签')
    viewnum = models.IntegerField('阅读次数')
    commentnum = models.IntegerField('评论次数')

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='博客')
    user = models.ForeignKey(User, verbose_name='用户')
    content = models.TextField('评论内容')
    created = models.DateTimeField('发布时间', auto_now_add=True)

    def __unicode__(self):
        return self.content