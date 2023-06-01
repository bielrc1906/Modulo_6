from django.shortcuts import render

from django.shortcuts import render
from .models import Plataforma
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PlataformaSerializer
from rest_framework import generics


class PlataformaRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer

class PlataformaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer

class PlataformaDelete(generics.DestroyAPIView):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer

class PlataformaUpdateAPIView(generics.UpdateAPIView):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer