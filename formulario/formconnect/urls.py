from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Vista inicial al correr el servidor
    path('', views.index, name='index'),
]
