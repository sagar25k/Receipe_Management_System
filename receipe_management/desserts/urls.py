from django.urls import path
from .views import add_dessert, show_desserts

urlpatterns = [
    path('desserts/', show_desserts, name='show_desserts'),
    path('add-dessert/', add_dessert, name='add_dessert'),
]
