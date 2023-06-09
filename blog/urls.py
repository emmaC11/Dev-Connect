from .import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PostListView.as_view(), name='homepage'),
    path(
        'about/',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    # path converter
    path(
        '<slug:slug>/',
        views.PostContentView.as_view(),
        name='post_content'
    ),
    path(
        'like/<slug:slug>',
        views.PostLikeView.as_view(),
        name='post_like'
    ),
    path(
        'comment/delete/<int:comment_id>/',
        views.DeleteCommentView.as_view(),
        name='delete_comment'
    ),
    path(
        'comment/edit/<int:comment_id>/',
        views.EditCommentView.as_view(),
        name='edit_comment'
    ),
    path(
        'post/delete/<slug:slug>',
        views.DeletePostView.as_view(),
        name='delete_post'
    ),
]
