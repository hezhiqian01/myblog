__author__ = 'Administrator'

from django.conf.urls import url
from . import views

app_name = 'MyBlog'
urlpatterns = [
    url(r'^register/', views.render(), name='register'),
]