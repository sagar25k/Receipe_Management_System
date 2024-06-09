from django.contrib import admin 
from django.urls import path, include,re_path
from django.conf.urls.static import static 
from django.conf import settings 
from django.contrib.auth import views as auth_views
# from django.contrib.auth import views as auth_views

from .views import index, header, footer, login, register,admindashboard, view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('index/', index, name='index'),
    path('header/', header, name='header'),
    path('footer/', footer, name='footer'),
    # path('recipeslist/', recipeslist, name='recipeslist'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('', view, name='view'),
    path('admindashboard/', admindashboard, name='admindashboard'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('addreceipe/', addreceipe, name='addreceipe'),
    path('accounts/', include('accounts.urls')),
    # path('recipe/', include('recipe.urls')),  # Ensure this is correct
    # path('recipe_details/', recipe_details, name='recipe_details'),
    path('', include('desserts.urls')), 
    path('', include('snacks.urls')), # Replace 'your_app_name' with the name of your app
    path('beverages/', include('beverages.urls')),
    path('icecreams/', include('icecreams.urls')),
    path('seafood/', include('seafood.urls')),
    path('veg/', include('veg.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('add_beverage/', include('beverages.urls')),
    re_path(r'^.*$', view, name='view'),

]

# Append the static files serving
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),