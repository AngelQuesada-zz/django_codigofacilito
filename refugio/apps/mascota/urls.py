from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreateView


app_name = "mascota"

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', MascotaCreateView.as_view(), name='mascota_crear'),
    path('lista', MascotaList.as_view(), name='mascota_listar'),
    path('editar/<int:id_mascota>/', mascota_edit, name='mascota_editar'),
    path('eliminar/<int:id_mascota>/', mascota_delete, name='mascota_eliminar'),
]
