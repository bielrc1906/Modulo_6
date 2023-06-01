from django.urls import path
from . import views

urlpatterns = [
    path('<str:nombreplataforma>', views.api_videojuego),
    path('<int:pk>', views.VideojuegoRetrieveAPIView.as_view()),
    path('create', views.VideojuegoListCreateAPIView.as_view()),
    path('delete/<int:pk>', views.VideojuegoDelete.as_view()),
    path('update/<int:pk>', views.VideojuegoUpdateAPIView.as_view()),
]