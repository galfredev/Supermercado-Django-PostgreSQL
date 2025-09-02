"""
views.py — Controladores de la app.
Incluye:
- Home (listado de productos)
- CRUD de productos (crear/editar/eliminar) con formularios de Django
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Product
from .forms import ProductForm

def home(request):
    """Vista principal: lista todos los productos disponibles."""
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'products': products})

def product_create(request):
    """Crea un nuevo producto usando ProductForm."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'core/product_form.html', {'form': form, 'title': 'Crear producto'})

def product_update(request, pk):
    """Edita un producto existente identificado por su PK."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'core/product_form.html', {'form': form, 'title': 'Editar producto'})

def product_delete(request, pk):
    """Confirma y elimina un producto existente."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Producto eliminado.')
        return redirect('home')
    return render(request, 'core/product_confirm_delete.html', {'product': product})
