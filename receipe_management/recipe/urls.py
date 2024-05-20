
from django.urls import path 

from . import views
from .views import recipe_details




urlpatterns = [

    path('<str:name>/', recipe_details, name='recipe_details'),
]





