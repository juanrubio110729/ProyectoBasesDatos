from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from app.forms import LibroDigitalForm
from app.mixins import ValidatePermissionRequiredMixin
from app.models import *
from django.core import serializers
import json

class LibroDigitalListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = LibroDigital
    template_name = 'librodigital/list.html'
    permission_required = 'app.view_librodigital'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for i in LibroDigital.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position+=1
            elif action == 'download':
                try:
                    libro = request.POST['parameters']
                    usuario = request.user.id
                    direccion_ip=request.META['REMOTE_ADDR']

                    descarga = Descargas(usuario_id=usuario, libro_id=libro, direccion_ip=direccion_ip)
                    descarga.save()
                except:
                    raise ValueError('No se pudo descargar el libro')
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de libros digitales'
        context['list_url'] = reverse_lazy('app:librodigital_list')
        context['create_url'] = reverse_lazy('app:librodigital_create')
        context['entity'] = 'Libros digitales'
        return context
    
class LibroDigitalCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = LibroDigital
    form_class = LibroDigitalForm
    template_name = 'librodigital/create.html'
    permission_required = 'app.add_librodigital'
    success_url = reverse_lazy('app:librodigital_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de un libro digital'
        context['entity'] = 'Libros digitales'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
    
class LibroDigitalUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = LibroDigital
    form_class = LibroDigitalForm
    template_name = 'librodigital/create.html'
    permission_required = 'app.change_librodigital'
    success_url = reverse_lazy('app:librodigital_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                self.object = self.get_object()  # Obtener el objeto a actualizar
                form = self.get_form()
                if form.is_valid():
                    form.save()  # Guardar los cambios en el objeto existente
                    data['success'] = 'Registro actualizado exitosamente'
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un libro digital'
        context['entity'] = 'Libros digitales'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
    
class LibroDigitalDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = LibroDigital
    template_name = 'librodigital/delete.html'
    permission_required = 'app.delete_areaconocimiento'
    success_url = reverse_lazy('app:librodigital_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un libro digital'
        context['entity'] = 'Libros digitales'
        context['list_url'] = self.success_url
        return context