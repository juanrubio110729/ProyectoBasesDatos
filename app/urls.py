from django.urls import path
from app.views.area_conocimiento_views import *
from app.views.autores_views import *
from app.views.dashboard_views import DashboardView
from app.views.descarga_views import DescargaListView
from app.views.editorial_views import *
from app.views.ejemplar_views import *
from app.views.libro_views import *
from app.views.librodigital_views import *
from app.views.multa_views import *
from app.views.prestamo_views import *
from app.views.solicitud_views import *

app_name= 'app'

urlpatterns = [
    #Dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #Area Conocimiento
    path('area_conocimiento/list/', AreaConocimientoListView.as_view(), name="area_conocimiento_list"),
    path('area_conocimiento/add/', AreaConocimientoCreateView.as_view(), name="area_conocimiento_create"),
    path('area_conocimiento/update/<str:pk>/', AreaConocimientoUpdateView.as_view(), name="area_conocimiento_update"),
    path('area_conocimiento/delete/<str:pk>/', AreaConocimientoDeleteView.as_view(), name="area_conocimiento_delete"),
    #Autores
    path('autores/list/', AutoresListView.as_view(), name="autores_list"),
    path('autores/add/', AutoresCreateView.as_view(), name="autores_create"),
    path('autores/update/<str:pk>/', AutoresUpdateView.as_view(), name="autores_update"),
    path('autores/delete/<str:pk>/', AutoresDeleteView.as_view(), name="autores_delete"),
    #Libros
    path('libro/list/', LibroListView.as_view(), name="libro_list"),
    path('libro/add/', LibroCreateView.as_view(), name="libro_create"),
    path('libro/update/<str:pk>/', LibroUpdateView.as_view(), name="libro_update"),
    path('libro/delete/<str:pk>/', LibroDeleteView.as_view(), name="libro_delete"),
    #Editoriales
    path('editoriales/list/', EditorialListView.as_view(), name="editorial_list"),
    path('editoriales/add/', EditorialCreateView.as_view(), name="editorial_create"),
    path('editorial/update/<str:pk>/', EditorialUpdateView.as_view(), name="editorial_update"),
    path('editorial/delete/<str:pk>/', EditorialDeleteView.as_view(), name="editorial_delete"),
    #Ejemplares
    path('ejemplar/list/', EjemplarListView.as_view(), name="ejemplar_list"),
    path('ejemplar/add/', EjemplarCreateView.as_view(), name="ejemplar_create"),
    path('ejemplar/update/<str:pk>/', EjemplarUpdateView.as_view(), name="ejemplar_update"),
    path('ejemplar/delete/<str:pk>/', EjemplarDeleteView.as_view(), name="ejemplar_delete"),
    #Libros digitales
    path('librodigital/list/', LibroDigitalListView.as_view(), name="librodigital_list"),
    path('librodigital/add/', LibroDigitalCreateView.as_view(), name="librodigital_create"),
    path('librodigital/update/<str:pk>/', LibroDigitalUpdateView.as_view(), name="librodigital_update"),
    path('librodigital/delete/<str:pk>/', LibroDigitalDeleteView.as_view(), name="librodigital_delete"),
    #Descargas
    path('descarga/list/', DescargaListView.as_view(), name="descarga_list"),
    #Solicitud libros nuevos
    path('solicitud/list/', SolicitudListView.as_view(), name="solicitud_list"),
    path('solicitud/add/', SolicitudCreateView.as_view(), name="solicitud_create"),
    path('solicitud/update/<str:pk>/', SolicitudUpdateView.as_view(), name="solicitud_update"),
    path('solicitud/delete/<str:pk>/', SolicitudDeleteView.as_view(), name="solicitud_delete"),
    #Prestamos
    path('prestamo/list/', PrestamoListView.as_view(), name="prestamo_list"),
    path('prestamo/add/', PrestamoCreateView.as_view(), name="prestamo_create"),
    path('prestamo/update/<str:pk>/', PrestamoUpdateView.as_view(), name="prestamo_update"),
    path('prestamo/delete/<str:pk>/', PrestamoDeleteView.as_view(), name="prestamo_delete"),
    #Multa
    path('multa/list/', MultaListView.as_view(), name="multa_list"),
    path('multa/add/', MultaCreateView.as_view(), name="multa_create"),
    path('multa/update/<str:pk>/', MultaUpdateView.as_view(), name="multa_update"),
    path('multa/delete/<str:pk>/', MultaDeleteView.as_view(), name="multa_delete"),
]