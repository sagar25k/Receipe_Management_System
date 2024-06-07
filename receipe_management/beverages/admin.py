from django.contrib import admin
from .models import BeveragesRecipe
from django.utils.safestring import mark_safe

@admin.register(BeveragesRecipe)
class BeveragesRecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url}" width="100" height="100" />')
        return "-"
    image_preview.short_description = 'Image Preview'
