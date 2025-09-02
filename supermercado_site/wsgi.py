"""
wsgi.py — Configuración WSGI para servidores como Gunicorn o uWSGI.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'supermercado_site.settings')
application = get_wsgi_application()
