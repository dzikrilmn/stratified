from django import forms
from .models import Product

class ProductEntryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']
