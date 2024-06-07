from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import IceCreamRecipe

@admin.register(IceCreamRecipe)
class IceCreamRecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'image_preview')
    search_fields = ('title', 'category')
    readonly_fields = ('created_at', 'updated_at', 'image_preview',)

    def image_preview(self, obj):
        if obj.image_url and obj.image_url.startswith('http'):
            return mark_safe(f'<img src="{obj.image_url}" width="100" height="100" />')
        return ""

    image_preview.short_description = 'Image Preview'
