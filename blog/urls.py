from .import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(), name='homepage'),
    # path converter
    path('<slug:slug>/', views.PostContentView.as_view(), name='post_content'),
]
