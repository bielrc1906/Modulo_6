from django.shortcuts import render

from django.shortcuts import render
from .models import Videojuego
from plataforma.models import Plataforma
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import VideojuegoSerializer
from plataforma.serializers import PlataformaSerializer
from rest_framework import generics


@api_view(['GET'])
def api_videojuego(request, nombreplataforma, *arg, **kwargs):

    data = {}
    
    instances = Videojuego.objects.filter(plataforma__icontains=nombreplataforma)
    if instances:
            data = VideojuegoSerializer(instances, many=True).data

    return Response(data)

class VideojuegoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer

class VideojuegoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer

class VideojuegoDelete(generics.DestroyAPIView):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer

class VideojuegoUpdateAPIView(generics.UpdateAPIView):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer