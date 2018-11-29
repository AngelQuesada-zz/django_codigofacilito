from django.contrib import admin
from django.urls import path

from apps.mascota.views import index, mascota_view

app_name = "mascota"

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', mascota_view, name='mascota_crear'),
]
