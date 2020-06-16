from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('single_blog', views.single_blog, name='single_blog'),
]