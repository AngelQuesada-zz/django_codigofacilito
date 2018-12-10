from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

# Create your views here.

def index(request):
    return render(request,'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:index')
    else:
        form = MascotaForm()
    
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_list(request):
    mascotas = Mascota.objects.all()
    context = {'mascotas':mascotas}
    return render (request, 'mascota/mascota_list.html', context)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'

class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = "mascota/mascota_form.html"
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaUpdateView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = "mascota/mascota_form.html"
    success_url = reverse_lazy('mascota:mascota_listar')


class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = "mascota/mascota_delete.html"
    success_url = reverse_lazy('mascota:mascota_listar')
