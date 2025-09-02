"""
models.py — Define las entidades del dominio del supermercado.
- Product: artículo disponible con precio y stock.
- Sale: cabecera de una venta.
- SaleItem: ítem de una venta, referencia a producto y cantidad.
"""
from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=30, unique=True, help_text="Código único del producto")
    name = models.CharField(max_length=120, help_text="Nombre descriptivo")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio unitario")
    stock = models.IntegerField(default=0, help_text="Cantidad disponible en stock")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Sale(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha/hora de creación de la venta")
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Venta #{self.pk} - {self.created_at:%Y-%m-%d %H:%M}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def line_total(self):
        return self.qty * self.unit_price

    def __str__(self):
        return f"{self.qty} x {self.product}"
