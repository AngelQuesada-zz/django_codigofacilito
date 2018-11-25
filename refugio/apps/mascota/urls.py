from django.contrib import admin
from django.urls import path

from apps.mascota.views import index

urlpatterns = [
    path('', index),
]
