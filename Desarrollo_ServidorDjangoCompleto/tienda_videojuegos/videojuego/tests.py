from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Videojuego

from django.contrib.auth.models import User as DjangoUser
from rest_framework.authtoken.models import Token
# Create your tests here.

class VideojuegoViewSetTest(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token.key)
        self.videojuego1 = Videojuego.objects.create(nombre='Fortnite', año=2017, plataforma='PS4')

    def test_videojuego_creation(self):
        url = '/videojuego/create'
        data = {'nombre': 'NBA', 'año': 2018, 'plataforma': 'PS4'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_restringir_put(self):
        url = f'/videojuego/videojuego_viewset/{self.videojuego1.id}/'
        data = {'nombre': 'Fortnite', 'año': 2019, 'plataforma': 'PS4'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 405)