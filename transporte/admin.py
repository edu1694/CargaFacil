from django.contrib import admin
from .models import SolicitudTransporte
# Register your models here.

@admin.register(SolicitudTransporte)
class SolicitudTransporteAdmin(admin.ModelAdmin):
    list_display = ('codigo_seguimiento', 'persona_origen', 'direccion_origen', 'persona_destino', 'direccion_destino', 'descripcion', 'estado')
    search_fields = ('codigo_seguimiento', 'persona_origen', 'persona_destino', 'estado')
    list_filter = ('estado',)
    