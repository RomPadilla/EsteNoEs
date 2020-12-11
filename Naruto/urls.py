from django.urls import path
from . import views

urlpatterns=[
    path('',views.InformacioneListView.as_view(),name='Naruto'),
]
