from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import SnacksRecipe

@admin.register(SnacksRecipe)
class SnacksRecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description', 'image_preview')
    search_fields = ('title', 'category')

    def image_preview(self, obj):
        return obj.image_url and obj.image_url.startswith('http') and mark_safe(f'<img src="{obj.image_url}" width="100" height="100" />')

    image_preview.short_description = 'Image Preview'
