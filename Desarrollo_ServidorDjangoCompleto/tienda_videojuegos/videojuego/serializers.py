from rest_framework import serializers

from .models import Videojuego

class VideojuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = ['nombre', 'año', 'plataforma']