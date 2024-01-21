from django import forms
from .models import SolicitudTransporte

class SolicitudTransporteForm(forms.ModelForm):
    class Meta:
        model = SolicitudTransporte
        exclude = ['codigo_seguimiento']