#coding: utf-8
__author__ = 'Administrator'

from .models import Blog
from django_redis import get_redis_connection
#from django.core.cache import cache
#from apscheduler.schedulers.background import BackgroundScheduler


RUNNING_TIMER = False
REDIS_DB = get_redis_connection('default')


def update_click(blog):
    if REDIS_DB.hexists('CLICKS', blog.id):
        REDIS_DB.hincrby('CLICKS', blog.id)
    else:
        REDIS_DB.hset('CLICKS', blog.id, blog.viewnum + 1)

def get_click(blog):
    if REDIS_DB.hexists('CLICKS', blog.id):
        return REDIS_DB.hget('CLICKS', blog.id)
    else:
        REDIS_DB.hset('CLICKS', blog.id, blog.viewnum)
        return blog.viewnum

def sync_click():

    for k in REDIS_DB.hkeys('CLICKS'):
        try:
            blog = Blog.objects.get(pk=k)
            cache_click = REDIS_DB.hget('CLICKS', k)
            if blog.viewnum != cache_click:
                blog.viewnum = cache_click
                blog.save()

        except:
            print('some problems happened')
            pass
