# coding: utf-8
from django.db import models
from users.models import User
import markdown
from django.utils.html import strip_tags
from markdownx.models import MarkdownxField

# Create your models here.



class Catagory(models.Model):
    name = models.CharField('名称', max_length=30)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return "%s" % self.name

class Tag(models.Model):
    name = models.CharField('名称', max_length=16)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return "%s" % self.name

class Blog(models.Model):
    title = models.CharField('标题', max_length=32)
    author = models.ForeignKey(User, verbose_name='作者')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    modified = models.DateTimeField('修改时间')
    excerpt = models.CharField('文章摘要', max_length=200, blank=True)
#    content = models.TextField('博客内容')
    content = MarkdownxField('博客内容')
    catagory = models.ForeignKey(Catagory, verbose_name='分类')
    tags = models.ManyToManyField(Tag,verbose_name='标签')
    viewnum = models.IntegerField('阅读次数')
    commentnum = models.IntegerField('评论次数')

    def increase_views(self):
        self.viewnum += 1
        self.save(update_fields=['viewnum'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.content))[:100]
        super(Blog, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return "%s" % self.title

   # def get_absolute_url(self):
    #    return reverse('blog:detail', kwargs={'pk':self.pk})
"""
class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='博客')
    user = models.ForeignKey(User, verbose_name='用户')
    content = models.TextField('评论内容')
    created = models.DateTimeField('发布时间', auto_now_add=True)

    def __unicode__(self):
        return self.content

    def __str__(self):
        return "%s" % self.content
"""


class Mymodel(models.Model):
    textfield = MarkdownxField()