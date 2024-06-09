from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_vegetarian, name='show_vegetarian'),
    path('add/', views.add_vegetarian, name='add_vegetarian'),
]
