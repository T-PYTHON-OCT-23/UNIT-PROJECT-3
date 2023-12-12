# car/forms.py
from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'year', 'image', 'color', 'seats', 'pags', 'air_conditioner', 'transmission_type', 'fuel_type', 'price']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),  # Customize the widget as needed
        }
