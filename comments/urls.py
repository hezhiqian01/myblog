__author__ = 'Administrator'

from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'comments'

urlpatterns = [
    url(r'^$', views.post_comment, name='post_comment'),
    url(r'^post_comment/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
