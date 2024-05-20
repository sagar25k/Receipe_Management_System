from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import Recipe


def recipe_details(request, name):
    recipe = get_object_or_404(Recipe,name=name)
    return render(request, 'recipe_details.html',{'recipe':recipe})