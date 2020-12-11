from django.shortcuts import render
from .models import Informaciones
from django.views import generic
# Create your views here.

class InformacioneListView(generic.ListView):
    model = Informaciones
    template_name='Naruto.html'
    context_object_name='Informaciones_list'
        
