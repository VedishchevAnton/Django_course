from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, increase_views

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_details/<int:pk>/', BlogDetailView.as_view(), name='blog_details'),
    path('blogs/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('increase_views/<int:pk>/', increase_views, name='increase_views'),

]
