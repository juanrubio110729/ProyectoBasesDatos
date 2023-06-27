from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from app.forms import PrestamoForm
from app.mixins import ValidatePermissionRequiredMixin
from app.models import *
from django.core import serializers
import json

class PrestamoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Prestamo
    template_name = 'prestamo/list.html'
    permission_required = 'app.view_prestamo'

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
                prestamos = Prestamo.objects.select_related('usuario').prefetch_related('ejemplar').all()
                for prestamo in prestamos:
                    item = prestamo.toJSON()
                    item['position'] = position

                    ejemplares = json.loads(item['ejemplar'])
                    numeros_ejemplares = [ejemplar['fields']['numero_ejemplar'] for ejemplar in ejemplares]
                    item['numeros_ejemplares'] = numeros_ejemplares
                    
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        print(data)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de prestamos'
        context['list_url'] = reverse_lazy('app:prestamo_list')
        context['create_url'] = reverse_lazy('app:prestamo_create')
        context['entity'] = 'Prestamos'
        return context
    
class PrestamoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamo/create.html'
    permission_required = 'app.add_prestamo'
    success_url = reverse_lazy('app:prestamo_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()  
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.usuario = request.user
                    instance.save()
                    form.save_m2m() #Guarda los ejemplares seleccionados
                    data['success'] = 'El prestamo se ha creado exitosamente.'
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de un prestamo'
        context['entity'] = 'Prestamos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
    
class PrestamoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Solicitud
    form_class = PrestamoForm
    template_name = 'prestamo/create.html'
    permission_required = 'app.change_prestamo'
    success_url = reverse_lazy('app:prestamo_list')
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
        context['title'] = 'Edición de un prestamo'
        context['entity'] = 'Prestamos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
    
class PrestamoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Prestamo
    template_name = 'prestamo/delete.html'
    permission_required = 'app.delete_prestamo'
    success_url = reverse_lazy('app:prestamo_list')
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
        context['title'] = 'Eliminación de un prestamo'
        context['entity'] = 'Prestamos'
        context['list_url'] = self.success_url
        return context