from django.urls import path
from .views import index,crear_solicitud, listar_solicitud, logouts, modificar_solicitud
urlpatterns = [
    path('', index, name='transporte_index'),
    path('contacto/',crear_solicitud, name='crear_solicitud'),
    path('listado/', listar_solicitud, name='listar_solicitud'),
    path('accounts/logout/', logouts, name='logout'),
    path('modificar_solicitud/<str:codigo_seguimiento>/', modificar_solicitud, name='modificar_solicitud'),
]

