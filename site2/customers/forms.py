# forms.py
from django import forms
from .models import Customer

class CustomerSignupForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'fullName','email','phone','address']  # Include other fields here
