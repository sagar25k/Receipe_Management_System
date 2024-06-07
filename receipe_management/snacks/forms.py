from django import forms
from .models import SnacksRecipe

class SnacksRecipeForm(forms.ModelForm):
    class Meta:
        model = SnacksRecipe
        fields = ['title', 'description', 'category', 'ingredients', 'instructions']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),
        }
