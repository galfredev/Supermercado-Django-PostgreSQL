# 🛒 Supermercado (Django + SQLite)

Aplicación web en **Django** para gestionar un supermercado (productos y ventas).  
Incluye **CRUD de productos**, panel **Django Admin**, y configuración lista con **SQLite**.

## ✨ Funcionalidades iniciales
- Listado de productos.
- Crear / Editar / Eliminar productos (CRUD).
- Admin de Django para gestión rápida.

## 🧰 Requisitos
- Python 3.10+
- pip

## 🚀 Puesta en marcha (local)
```bash
# 1) (opcional) Crear y activar entorno virtual
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

# 2) Instalar dependencias
pip install -r requirements.txt

# 3) Migraciones y superusuario
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 4) Correr el servidor
python manage.py runserver
```
Abrí http://127.0.0.1:8000 para ver el sitio y /admin para el panel.

## 🗂️ Estructura
```
Supermercado/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── supermercado_site/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── core/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    └── templates/core/
        ├── home.html
        ├── product_form.html
        └── product_confirm_delete.html
```

## 👥 Autores
- Valentino Galfré
- Equipo

> Proyecto educativo: base preparada para extender a ventas, tickets e informes.
