from django.urls import path
from . import views

urlpatterns=[
    path('',views.PersonajeListView.as_view(),name='ListaPersonajes'),
    path('personaje/<int:pk>', views.PersonajeDetailView.as_view(),name='personaje-detail'),
    path('personaje/<int:pk>/delete/',views.PersonajeDelete.as_view(),name='personaje_delete'),
]
