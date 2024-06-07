from django.shortcuts import render, get_object_or_404,redirect
from django.utils.dateparse import parse_duration
# from recipe.models import Recipe, RecipeType
from django.utils import timezone
from datetime import datetime, timedelta
from accounts.models import Profile

from django.contrib.auth.decorators import login_required

# @login_required
# def index(request):
#     user_profile = Profile.objects.get(user=request.user)
#     return render(request, 'index.html',{'user_type':user_profile.user_type})

@login_required
def view(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
        return render(request, 'view.html', {'user_type': user_profile.user_type})
    except Profile.DoesNotExist:
        # Handle the case where the profile does not exist
        return redirect('register')  # or another appropriate view
    
    
def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def footer(request):
    return render(request, "footer.html")

def header(request):
    return render(request, "header.html")

# def recipeslist(request):
#     r = Recipe.objects.all()
#     return render(request, "recipeslist.html", {'r': r})

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

# @login_required
# def view(request):
#     return render(request, "view.html")


def admindashboard(request):
    return render(request, "admindashboard.html")


# def recipe_details(request, name):
#     recipe = get_object_or_404(Recipe, name=name)
#     return render(request, 'recipe_details.html', {'recipe': recipe})

# @login_required
# def addreceipe(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         description = request.POST['description']
#         prep_time_str = request.POST['prep_time']
#         cook_time_str = request.POST['cook_time']
#         servings = request.POST['servings']
#         instructions = request.POST['instructions']
#         recipe_type_name = request.POST['recipe_type']
#         created_date_str = request.POST['created_date']

#         # Parse prep_time and cook_time strings into timedelta objects
#         prep_time = parse_duration(prep_time_str)
#         cook_time = parse_duration(cook_time_str)

#         # Ensure RecipeType instance exists or create a new one
#         recipe_type, created = RecipeType.objects.get_or_create(name=recipe_type_name)

#         # Parse created_date string into datetime object
#         try:
#             created_date = datetime.strptime(created_date_str, '%Y-%m-%d %H:%M:%S')
#         except ValueError:
#             created_date = timezone.now()

#         recipe = Recipe(
#             name=name,
#             description=description,
#             prep_time=prep_time,
#             cook_time=cook_time,
#             servings=servings,
#             instructions=instructions,
#             recipe_type=recipe_type,
#             created_date=created_date
#         )
#         recipe.save()
#         return render(request, 'success.html', {'recipe': recipe})

#     return render(request, 'addreceipe.html')
