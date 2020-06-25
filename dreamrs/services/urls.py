from django.urls import path
from . import views

urlpatterns = [
    path('apartment', views.apartment, name='Apartment'),
    #path('elements', views.elements, name='elements'),
    path('services', views.services, name='services'),
    path('project', views.project, name='project'),
]