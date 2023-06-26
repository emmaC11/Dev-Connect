from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import UserCommentForm


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostContentView(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # pass info to render method
        return render(request, "post_content.html", {
            "post": post,
            "comments": comments,
            "commented": False,
            "liked": liked,
            "comment_form": UserCommentForm()
        },)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        comment_content = UserCommentForm(data=request.POST)
        if comment_content.is_valid():
            # get user details
            comment_content.instance.email = request.user.email
            comment_content.instance.name = request.user.username
            comment = comment_content.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_content = UserCommentForm()

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        # pass info to render method
        return render(request, "post_content.html", {
            "post": post,
            "comments": comments,
            "commented": True,
            "liked": liked,
            "comment_form": UserCommentForm()
        },)
