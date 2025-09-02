"""
admin.py — Registro de modelos en el panel de administración de Django.
Permite crear/editar/borrar productos y ventas desde /admin.
"""
from django.contrib import admin
from .models import Product, Sale, SaleItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'price', 'stock', 'created_at')
    search_fields = ('code', 'name')
    list_filter = ('created_at',)

admin.site.register(Sale)
admin.site.register(SaleItem)
