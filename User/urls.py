from django.urls import path
from . import views

urlpatterns=[
    path('',views.user,name='User'),
    path('FormularioRegistro/', views.formularioRegistro, name="register"),
]
