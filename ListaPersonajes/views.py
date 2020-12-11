from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Personaje
from django.views import generic

class PersonajeListView(generic.ListView):
    model = Personaje
    template_name='ListaPersonajes.html'
    context_object_name='Personaje_list'

class PersonajeDelete(DeleteView):
    model=Personaje
    success_url=reverse_lazy('ListaPersonajes')

class PersonajeDetailView(generic.DetailView):
    model=Personaje

