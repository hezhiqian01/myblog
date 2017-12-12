__author__ = 'Administrator'

from ..models import Blog, Catagory, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag()
def get_recent_blogs(num=5):
    return Blog.objects.all().order_by('-created')[:num]

@register.simple_tag()
def archives():
    return Blog.objects.dates('created', 'month', order='DESC')

@register.simple_tag()
def get_catagories():
    return Catagory.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)

@register.simple_tag()
def get_tags():
    return Tag.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)
