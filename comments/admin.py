# coding: utf-8
from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'user','content', 'created')
    search_fields = ('content',)
 #   inlines = [BlogInline, UserInline]

admin.site.register(Comment, CommentAdmin)