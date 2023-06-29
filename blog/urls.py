from .import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PostListView.as_view(), name='homepage'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('addpost/', TemplateView.as_view(template_name='add_post.html'), name='add_post'),
    # path converter
    path('<slug:slug>/', views.PostContentView.as_view(), name='post_content'),
    path('like/<slug:slug>', views.PostLikeView.as_view(), name='post_like'),
    path('comment/delete/<int:comment_id>/', views.DeleteCommentView.as_view(), name='delete_comment'),

]
