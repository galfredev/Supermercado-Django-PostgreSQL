"""
urls.py (proyecto) — Enruta las URLs principales del sitio hacia la app core y el admin.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Comentario: delega a las rutas de la app core
]
