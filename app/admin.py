from django.contrib import admin
from app.models import * 

# Register your models here.
admin.site.register(Libro)
admin.site.register(Areaconocimiento)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Ejemplar)
admin.site.register(LibroDigital)