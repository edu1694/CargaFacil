from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from transporte.models import SolicitudTransporte
from .serializers import SolicitudTransporteSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt #para que no pida tocken de acceso
@api_view(['GET','POST']) #solo acepte perticiones GET
def listado_solicitud(request):
    if request.method == 'GET':
        solicitud = SolicitudTransporte.objects.all()
        serializer = SolicitudTransporteSerializer(solicitud, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SolicitudTransporteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt #para que no pida tocken de acceso
@api_view(['GET','PUT','DELETE']) #solo acepte perticiones GET
def vista_solicitud(request, id):
    if request.method == 'GET':
        try:
            solicitud = SolicitudTransporte.objects.get(codigo_seguimiento=id)
        except SolicitudTransporte.DoesNotExist:
            return Response(status=status.HTPP_404_NOT_FOUND)
        serializer = SolicitudTransporteSerializer(solicitud)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            solicitud = SolicitudTransporte.objects.get(codigo_seguimiento=id)
        except SolicitudTransporte.DoesNotExist:
            return Response(status=status.HTPP_404_NOT_FOUND)
        data = JSONParser().parse(request)
        serializer = SolicitudTransporteSerializer(solicitud, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTPP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            solicitud = SolicitudTransporte.objects.get(codigo_seguimiento=id)
        except SolicitudTransporte.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
