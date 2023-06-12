from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)

class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    summernote_fields = ('content')
    search_fields = ['title', 'content']