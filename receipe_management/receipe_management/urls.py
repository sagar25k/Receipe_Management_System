from django.contrib import admin 
from django.urls import path, include,re_path
from django.conf.urls.static import static 
from django.conf import settings 
from django.contrib.auth import views as auth_views

from .views import index, header, footer, recipeslist, login, register, addreceipe, recipe_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('header/', header, name='header'),
    path('footer/', footer, name='footer'),
    path('recipeslist/', recipeslist, name='recipeslist'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('addreceipe/', addreceipe, name='addreceipe'),
    path('accounts/', include('accounts.urls')),
    path('recipe/', include('recipe.urls')),  # Ensure this is correct
    path('recipe_details/', recipe_details, name='recipe_details'),
    re_path(r'^.*$', index, name='index'),

]

# Append the static files serving
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)