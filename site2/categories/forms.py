# forms.py
from django import forms
from .models import Category

class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']  # Include other fields here
