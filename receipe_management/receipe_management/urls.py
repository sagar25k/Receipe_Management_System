from django.contrib import admin 
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 

from .views import index, header, footer, recipeslist, login, register, addreceipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('header/', header, name='header'),
    path('footer/', footer, name='footer'),
    path('recipeslist/', recipeslist, name='recipeslist'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('addreceipe/', addreceipe, name='addreceipe'),
    path('accounts/', include('accounts.urls')),
    path('recipe/', include('recipe.urls')),  # Ensure this is correct
]

# Append the static files serving
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
