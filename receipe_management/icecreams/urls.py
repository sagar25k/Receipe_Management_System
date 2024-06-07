from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_icecream, name='add_icecream'),
    path('', views.show_icecreams, name='show_icecreams'),
]
