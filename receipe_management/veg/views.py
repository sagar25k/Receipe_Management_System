from django.shortcuts import render, redirect
from .models import VegetarianRecipe
from .forms import VegetarianRecipeForm

def show_vegetarian(request):
    recipes = VegetarianRecipe.objects.all()
    return render(request, 'show_vegetarian.html', {'recipes': recipes})

def add_vegetarian(request):
    if request.method == 'POST':
        form = VegetarianRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_vegetarian')
    else:
        form = VegetarianRecipeForm()
    return render(request, 'add_vegetarian.html', {'form': form})
