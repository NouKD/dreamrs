from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('forgot', views.forgot, name='forgot'),
    path('login', views.login, name='login'),
]