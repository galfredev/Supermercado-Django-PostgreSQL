#!/usr/bin/env python
"""
manage.py — Punto de entrada para administrar el proyecto Django (comandos como runserver, migrate).
"""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'supermercado_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y disponible en tu entorno?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
