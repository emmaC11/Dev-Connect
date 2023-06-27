from .models import Comment, Post
from django import forms

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'category',
            'image'
        ]
