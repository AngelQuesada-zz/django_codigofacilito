from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.mascota.views import *


app_name = "mascota"

urlpatterns = [
    path('', login_required(index), name='index'),
    path('nuevo', login_required(MascotaCreateView.as_view()), name='mascota_crear'),
    path('lista', login_required(MascotaList.as_view()), name='mascota_listar'),
    path('editar/<int:pk>/', login_required(MascotaUpdateView.as_view()), name='mascota_editar'),
    path('eliminar/<int:pk>/', login_required(MascotaDeleteView.as_view()), name='mascota_eliminar'),
    # path('listado/', listado, name='listado'),
]
