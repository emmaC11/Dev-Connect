from .models import Comment, Post
from django import forms

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)