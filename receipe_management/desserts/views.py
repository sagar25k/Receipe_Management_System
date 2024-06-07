from django.shortcuts import render
from .models import DessertRecipe

def show_desserts(request):
    recipes = DessertRecipe.objects.all()
    return render(request, 'show_desserts.html', {'recipes': recipes})


from django.shortcuts import render, redirect
from .models import DessertRecipe
from .forms import DessertRecipeForm

def add_dessert(request):
    if request.method == 'POST':
        form = DessertRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_desserts')  # Redirect to the desserts list page
    else:
        form = DessertRecipeForm()
    return render(request, 'add_desserts.html', {'form': form})

def show_desserts(request):
    recipes = DessertRecipe.objects.all()
    return render(request, 'show_desserts.html', {'recipes': recipes})
