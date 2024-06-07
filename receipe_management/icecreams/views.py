from django.shortcuts import render, redirect
from .forms import IceCreamRecipeForm
from .models import IceCreamRecipe

def add_icecream(request):
    if request.method == 'POST':
        form = IceCreamRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_icecreams')
    else:
        form = IceCreamRecipeForm()
    return render(request, 'add_icecream.html', {'form': form})

def show_icecreams(request):
    recipes = IceCreamRecipe.objects.all()
    return render(request, 'show_icecreams.html', {'recipes': recipes})
