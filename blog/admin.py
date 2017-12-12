from django.contrib import admin
from .models import Blog,Tag, Catagory, Mymodel
from users.models import User
from comments.models import Comment
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.

"""
class TagInline(admin.TabularInline):
    model = Tag

class CatagoryInline(admin.TabularInline):
    model = Catagory
"""

class CommentInline(admin.TabularInline):
    model = Comment

class UserInline(admin.StackedInline):
    model = User


class BlogAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'excerpt', 'author', 'created','catagory')
    search_fields = ['title', 'content']
    list_display_links = ('title',)
    list_filter = ('title',)
    inlines = [CommentInline]


class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Blog,BlogAdmin)
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.register(Mymodel, MarkdownxModelAdmin)
