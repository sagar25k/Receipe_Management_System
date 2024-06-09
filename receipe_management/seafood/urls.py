from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_seafood, name='show_seafood'),
    path('add/', views.add_seafood, name='add_seafood'),
]
