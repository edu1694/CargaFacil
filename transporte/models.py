from django.db import models
from django.utils.crypto import get_random_string

class SolicitudTransporte(models.Model):
    ESTADOS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    )
    codigo_seguimiento = models.CharField(max_length=20, unique=True, primary_key=True)
    persona_origen = models.CharField(max_length=100)
    direccion_origen = models.CharField(max_length=255)
    persona_destino = models.CharField(max_length=100)
    direccion_destino = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default='pendiente')

    def __str__(self):
        return f"Solicitud {self.codigo_seguimiento} - {self.estado}"

    def save(self, *args, **kwargs):
        if not self.codigo_seguimiento:
            # Genera un código único
            self.codigo_seguimiento = self.generar_codigo_unico()
        super(SolicitudTransporte, self).save(*args, **kwargs)

    @staticmethod
    def generar_codigo_unico():
        length = 20
        while True:
            codigo = get_random_string(length=length)
            if not SolicitudTransporte.objects.filter(codigo_seguimiento=codigo).exists():
                break
        return codigo
