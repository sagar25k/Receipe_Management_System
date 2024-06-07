from django.shortcuts import render, redirect
from .models import BeveragesRecipe
from .forms import BeveragesRecipeForm

def add_beverage(request):
    if request.method == 'POST':
        form = BeveragesRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_beverages')
    else:
        form = BeveragesRecipeForm()
    return render(request, 'add_beverage.html', {'form': form})

def show_beverages(request):
    recipes = BeveragesRecipe.objects.all()
    return render(request, 'show_beverages.html', {'recipes': recipes})
