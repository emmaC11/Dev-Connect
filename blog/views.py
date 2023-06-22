from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class PostContentView(View):
    def get(self, request, slug, *args, **kwargs):
        
