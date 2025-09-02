"""
apps.py — Configuración de la app 'core' para Django.
"""
from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
