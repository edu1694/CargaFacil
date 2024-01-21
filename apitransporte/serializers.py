from rest_framework import serializers
from transporte.models import SolicitudTransporte


class SolicitudTransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudTransporte
        fields = '__all__'  # Incluye todos los campos
        read_only_fields = ('codigo_seguimiento', 'estado')
