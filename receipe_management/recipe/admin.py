from django.contrib import admin

from recipe.models import Recipe,RecipeType

admin.site.register(Recipe)
admin.site.register(RecipeType)