from django import forms
from .models import BeveragesRecipe

class BeveragesRecipeForm(forms.ModelForm):
    created_at = forms.DateTimeField(required=False, widget=forms.widgets.DateTimeInput(attrs={'readonly': 'readonly'}))
    updated_at = forms.DateTimeField(required=False, widget=forms.widgets.DateTimeInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = BeveragesRecipe
        fields = ['title', 'description', 'category', 'ingredients', 'instructions']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),
        }
