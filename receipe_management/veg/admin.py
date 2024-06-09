from django.contrib import admin
from .models import VegetarianRecipe
from django.utils.html import mark_safe

class VegetarianRecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'image_preview')
    readonly_fields = ('created_at', 'image_preview')
    
    def image_preview(self, obj):
        return obj.image_url and obj.image_url.startswith('http') and mark_safe(f'<img src="{obj.image_url}" width="100" height="100" />')

    image_preview.short_description = 'Image Preview'

admin.site.register(VegetarianRecipe, VegetarianRecipeAdmin)
