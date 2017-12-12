# coding: utf-8
from django.db import models

# Create your models here.

class Comment(models.Model):
    blog = models.ForeignKey('blog.Blog', verbose_name='博客')
    user = models.ForeignKey('users.User', verbose_name='用户')
    content = models.TextField('评论内容')
    created = models.DateTimeField('发布时间', auto_now_add=True)

    def __unicode__(self):
        return self.content

    def __str__(self):
        return "%s" % self.content
