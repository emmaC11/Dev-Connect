from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=400, unique=True)
    slug = models.SlugField(max_length=400, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="devconnect_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    category = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='devconnect_likes', blank=True)

    class Meta:
        # order posts/articles via created on field
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def like_count(self):
        return self.likes.count()

class Comment(models.model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    fname = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        # order comments via created on field - ascending order
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
