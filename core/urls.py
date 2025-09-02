"""
urls.py (app core) — Define las rutas específicas de la app (home y CRUD de productos).
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # CRUD productos
    path('productos/nuevo/', views.product_create, name='product_create'),
    path('productos/<int:pk>/editar/', views.product_update, name='product_update'),
    path('productos/<int:pk>/eliminar/', views.product_delete, name='product_delete'),
]
