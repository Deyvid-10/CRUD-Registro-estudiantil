from django.urls import path
from .views import Inicio, Ver, Agregar, Editar, Eliminar

urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
    path('ver/<int:pk>', Ver.as_view(), name="ver"),
    path("agregar", Agregar.as_view(), name="agregar"),
    path('editar/<int:pk>', Editar.as_view(), name="editar"),
    path('eliminar/<int:pk>', Eliminar.as_view(), name="eliminar"),
    ]