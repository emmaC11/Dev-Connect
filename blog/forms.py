from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget

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

        widgets = {
            'content': SummernoteInplaceWidget()
        }
