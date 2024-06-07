from django.urls import path
from .views import show_snacks, add_snacks

urlpatterns = [
    path('snacks/', show_snacks, name='show_snacks'),
    path('add-snacks/', add_snacks, name='add_snacks'),
]
