__author__ = 'Administrator'

from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^catagory/(?P<pk>[0-9]+)/$', views.CatagoryView.as_view(), name='catagory'),
    url(r'tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),

]
