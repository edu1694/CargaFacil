from django.shortcuts import get_object_or_404, redirect, render
from .models import SolicitudTransporte
from .forms import SolicitudTransporteForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def index(request):
    
    if request.method == 'POST':
        # buscar el codigo de seguimiento
        codigo_seguimiento = request.POST.get('codigo_seguimiento', '')
        # Realiza la búsqueda en la base de datos
        resultados = SolicitudTransporte.objects.filter(codigo_seguimiento=codigo_seguimiento).first()
        return render(request, 'index.html', {'resultados': resultados, 'codigo_seguimiento': codigo_seguimiento})
    
    return render(request, 'index.html')
@csrf_protect
def crear_solicitud(request):
    data = {
        'form': SolicitudTransporteForm()
    }
    if request.method == 'POST':
        solicitud = SolicitudTransporteForm(data=request.POST)
        if solicitud.is_valid():
            solicitud.save()
        else:
            data["form"] = solicitud

    return render(request, 'crearsoli.html', data)

def listar_solicitud(request):
    # Recuperar el término de búsqueda del request GET
    codigo_seguimiento_query = request.GET.get('codigo_seguimiento', '')

    # Filtrar las solicitudes por código de seguimiento si se proporciona un término de búsqueda
    if codigo_seguimiento_query:
        solicitudes = SolicitudTransporte.objects.filter(codigo_seguimiento__icontains=codigo_seguimiento_query)
        print(solicitudes)  # Depuración para ver qué se recupera
    else:
        solicitudes = SolicitudTransporte.objects.all()

    # Pasar las solicitudes al contexto de la plantilla HTML
    return render(request, 'listarsoli.html', {'solicitudes': solicitudes})

def logouts(request):
    logout(request)
    return redirect('transporte_index')

def modificar_solicitud(request, codigo_seguimiento):
    codigo_seguimiento = get_object_or_404(SolicitudTransporte, codigo_seguimiento=codigo_seguimiento)
    if request.method == "POST":
        nuevo_estado = request.POST.get('estado')
        codigo_seguimiento.estado = nuevo_estado
        codigo_seguimiento.save()
        return redirect('listar_solicitud')

    return render(request, 'modificar_solicitud.html', {'solicitud': codigo_seguimiento, 'ESTADOS_CHOICES': SolicitudTransporte.ESTADOS_CHOICES})
