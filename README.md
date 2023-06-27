# Aplicacion Biblioteca | Django
Este es una aplicación web para modelar la base de datos de una biblioteca de la Universidad del Valle. Desarrollada con Django como Framework Principal, complementado librerias como Bootstrap, Select2 y Datatable para el DOM.

#### CREAR ENTORNO VIRTUAL
Cuando el OS es windows:
```html
python -m venv venv
```
Cuando el OS es Linux o Mac:
```html
python3 -m venv venv
```

#### ACTIVAR ENTORNO VIRTUAL
Cuando el OS es windows:
```html
venv\Scripts\activate.bat
```
Cuando el OS es Linux o Mac:
```html
source venv/bin/activate
```
#### INSTALAR DEPENDENCIAS
```html
python -m pip install -r requirements.txt
```

#### CREACION BASE DE DATOS
##### Crea tu base de datos POSTGRESQL en tu gestor, en el Settings.py del proyecto, esta de nombre por defecto 'db'

#### MIGRACIONES
```html
python3 manage.py makemigrations
```
```html
python3 manage.py migrate
```

#### ARRANCAR PROYECTO
```html
python manage.py runserver
```
#### CREACION SUPER USUARIO
```html
python3 manage.py createsuperuser
```

#### GESTIONAR ADMIN, USUARIOS Y PERMISOS
```html
http://127.0.0.1:8000/admin/
```