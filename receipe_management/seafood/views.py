from django.shortcuts import render, redirect
from .models import SeafoodRecipe
from .forms import SeafoodRecipeForm

def show_seafood(request):
    recipes = SeafoodRecipe.objects.all()
    return render(request, 'show_seafood.html', {'recipes': recipes})

def add_seafood(request):
    if request.method == 'POST':
        form = SeafoodRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_seafood')
    else:
        form = SeafoodRecipeForm()
    return render(request, 'add_seafood.html', {'form': form})
