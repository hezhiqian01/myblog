__author__ = 'Administrator'

from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.user_login, name='login')
]