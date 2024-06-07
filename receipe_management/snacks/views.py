from django.shortcuts import render, redirect
from .models import SnacksRecipe
from .forms import SnacksRecipeForm

def show_snacks(request):
    recipes = SnacksRecipe.objects.all()
    return render(request, 'show_snacks.html', {'recipes': recipes})

def add_snacks(request):
    if request.method == 'POST':
        form = SnacksRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_snacks')
    else:
        form = SnacksRecipeForm()
    return render(request, 'add_snacks.html', {'form': form})
