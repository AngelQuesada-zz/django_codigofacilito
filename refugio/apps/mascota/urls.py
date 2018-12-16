from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.mascota.views import *


app_name = "mascota"

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', MascotaCreateView.as_view(), name='mascota_crear'),
    path('lista', MascotaList.as_view(), name='mascota_listar'),
    path('editar/<int:pk>/', MascotaUpdateView.as_view(), name='mascota_editar'),
    path('eliminar/<int:pk>/', MascotaDeleteView.as_view(), name='mascota_eliminar'),
]
