from django import forms
from .models import IceCreamRecipe

class IceCreamRecipeForm(forms.ModelForm):
    class Meta:
        model = IceCreamRecipe
        fields = ['title', 'description', 'category', 'ingredients', 'instructions', 'image_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
        }
