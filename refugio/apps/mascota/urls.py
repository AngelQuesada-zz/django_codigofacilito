from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete

app_name = "mascota"

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', mascota_view, name='mascota_crear'),
    path('lista', mascota_list, name='mascota_listar'),
    path('editar/<int:id_mascota>/', mascota_edit, name='mascota_editar'),
    path('eliminar/<int:id_mascota>/', mascota_delete, name='mascota_eliminar'),
]
