from django import forms
from .models import Product

class ProductEntryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']  # Include image field

        widgets = {
            'name': forms.TextInput(attrs={'class': 'border p-2 w-full rounded text-black'}),
            'price': forms.NumberInput(attrs={'class': 'border p-2 w-full rounded text-black'}),
            'description': forms.Textarea(attrs={'class': 'border p-2 w-full rounded text-black'}),
            'image': forms.ClearableFileInput(attrs={'class': 'border p-2 w-full rounded text-white'}),  # For image upload
        }
