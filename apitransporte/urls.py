from django.urls import path
from . import views

urlpatterns = [
    path('v1/solicitud', views.listado_solicitud, name='lista_solicitud'),
    path('v1/solicitud/<id>', views.vista_solicitud, name='vista_solicitud'),
]