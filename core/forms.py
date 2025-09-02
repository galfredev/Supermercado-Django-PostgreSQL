"""
forms.py — Formularios de Django para crear/editar productos desde el frontend.
"""
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'name', 'price', 'stock']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código único'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }
