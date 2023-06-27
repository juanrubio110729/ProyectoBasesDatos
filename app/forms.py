from django.forms import *
from django import forms

from app.models import Areaconocimiento, Autor, Editorial, Ejemplar, Libro, LibroDigital, Multa, Prestamo, Solicitud

class AreaConocimientoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo_area'].widget.attrs['autofocus'] = True

    class Meta:
        model = Areaconocimiento
        fields = '__all__'
        widgets = {
            'codigo_area': TextInput(
                attrs={
                    'placeholder': 'Ingrese un codigo',
                }
            ),
            'nombre_area': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del área',
                }
            ),
            'desc_area': TextInput(
                attrs={
                    'placeholder': 'De una descripción del área',
                }
            ),
            'cod_area_contenida': Select(
                attrs={
                    'class': 'select2',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        try:
            form = super().save(commit=False)
            form.codigo_area = form.codigo_area.upper() # Convierte el campo 'codigo_area' a mayúsculas
            form.nombre_area = form.nombre_area.upper() # Convierte el campo 'nombre_area' a mayúsculas
            if self.is_valid():
                if commit:
                    form.save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class AutorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo_autor'].widget.attrs['autofocus'] = True

    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'primer_nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el primer nombre',
                }
            ),
            'segundo_nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el segundo nombre',
                }
            ),
            'primer_apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese el primer apellido',
                }
            ),
            'segundo_apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese el segundo apellido',
                }
            ),
        }
        
    def save(self, commit=True):
        data = {}
        try:
            form = super().save(commit=False)
            form.codigo_autor = form.codigo_autor.upper() # Convierte el campo 'codigo_autor' a mayúsculas
            if self.is_valid():
                if commit:
                    form.save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
        
class EditorialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo_editorial'].widget.attrs['autofocus'] = True

    class Meta:
        model = Editorial
        fields = '__all__'
        widgets = {
            'codigo_editorial': TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo de la editorial: ED001',
                }
            ),
            'nombre_editorial': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la editorial',
                }
            ),
            'pagina_web': TextInput(
                attrs={
                    'placeholder': 'http://bibliotecaunivalle.edu.co',
                }
            ),
            'pais_origen': TextInput(
                attrs={
                    'placeholder': 'Ingrese el pais de Origen',
                }
            ),
        }
        
    def save(self, commit=True):
        data = {}
        try:
            form = super().save(commit=False)
            form.codigo_editorial = form.codigo_editorial.upper() # Convierte el campo 'codigo_editorial' a mayúsculas
            form.nombre_editorial = form.nombre_editorial.upper() # Convierte el campo 'nombre_editorial' a mayúsculas
            if self.is_valid():
                if commit:
                    form.save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class LibroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['isbn'].widget.attrs['autofocus'] = True

    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'isbn': TextInput(
                attrs={
                    'placeholder': 'Ingrese el ISBN del libro',
                }
            ),
            'titulo': TextInput(
                attrs={
                    'placeholder': 'Escribe el titulo del libro',
                }
            ),
            'anio_publicacion': TextInput(
                attrs={
                    'placeholder': 'Escribe el año de publicacion del libro',
                }
            ),
            'numero_pagina': TextInput(
                attrs={
                    'placeholder': 'Escribe la cantidad de paginas',
                }
            ),
            'codigo_area': Select(
                attrs={
                    'class':'select2'
                }
            ),
            'codigo_editorial': Select(
                attrs={
                    'class':'select2'
                }
            ),
            'autores': forms.SelectMultiple(
                attrs={
                    'class':'select2'
                }
            ),
        }
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class EjemplarForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero_ejemplar'].widget.attrs['autofocus'] = True

    class Meta:
        model = Ejemplar
        fields = '__all__'
        widgets = {
            'libro': Select(
                attrs={
                    'class':'select2'
                }
            ),
        }
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class LibroDigitalForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = LibroDigital
        fields = '__all__'
        widgets = {
            'libro': Select(
                attrs={
                    'class': 'select2'
                }
            ),
            'url': TextInput(
                attrs={
                    'placeholder': 'http://ejemplourlvalida.com'
                }
            )
        }
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class SolicitudForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'isbn': TextInput(
                attrs={
                    'placeholder': 'Escriba el ISBN del libro que desea'
                }
            ),
            'titulo': TextInput(
                attrs={
                    'placeholder': 'Escriba el titulo de su libro'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Escriba por que solicita el libro',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }
        exclude = ['usuario']
        
    def save(self, commit=True, user=None):
        data = {}
        instance = super().save(commit=False)
        if user:
            instance.usuario = user
        if commit:
            instance.save()
        return instance
    
class PrestamoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Prestamo
        fields = '__all__'
        widgets = {
            'ejemplar': forms.SelectMultiple(
                attrs={
                    'class':'select2'
                }
            ),
        }
        exclude = ['fecha_realizacion', 'fecha_devolucion', 'usuario']
        
    def save(self, commit=True, user=None):
        data = {}
        instance = super().save(commit=False)
        if user:
            instance.usuario = user
        if commit:
            instance.save()
        return instance
    

class MultaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Multa
        fields = '__all__'
        widgets = {
            'usuario': Select(
                attrs={
                    'class':'select2'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Escriba por que solicita el libro',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data