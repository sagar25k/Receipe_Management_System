from django.urls import path
from .views import add_beverage, show_beverages

urlpatterns = [
    path('add/', add_beverage, name='add_beverage'),
    path('', show_beverages, name='show_beverages'),
]
