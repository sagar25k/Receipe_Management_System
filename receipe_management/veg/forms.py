from django import forms
from .models import VegetarianRecipe

class VegetarianRecipeForm(forms.ModelForm):
    class Meta:
        model = VegetarianRecipe
        fields = ['title', 'description', 'category', 'ingredients', 'instructions']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),
        }
