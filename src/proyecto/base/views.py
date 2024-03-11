from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Registro

# Create your views here.

class Inicio(ListView):
    model = Registro
    template_name = "base/inicio.html"
    context_object_name = "registro"

class Ver(DetailView):
    model = Registro
    template_name = "base/ver.html"
    context_object_name = "registro"

class Agregar(CreateView):
    model = Registro
    template_name = "base/crear.html"
    fields = "__all__"
    success_url = reverse_lazy("inicio")

class Editar(UpdateView):
    model = Registro
    template_name = "base/editar.html"
    fields = "__all__"
    success_url = reverse_lazy("inicio")

class Eliminar(DeleteView):
    model = Registro
    template_name = "base/eliminar.html"
    success_url = reverse_lazy("inicio")
    context_object_name = "registro"