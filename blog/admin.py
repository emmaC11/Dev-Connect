from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status','created_on')
    prepopulated_fields = {'slug':('title',)}
    summernote_fields = ('content')
    search_fields = ['title', 'content']

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):