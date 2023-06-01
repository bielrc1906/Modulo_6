from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.PlataformaRetrieveAPIView.as_view()),
    path('create', views.PlataformaListCreateAPIView.as_view()),
    path('delete/<int:pk>', views.PlataformaDelete.as_view()),
    path('update/<int:pk>', views.PlataformaUpdateAPIView.as_view()),
]