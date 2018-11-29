from django.shortcuts import render, redirect, get_object_or_404
from .forms import PerritoForm
from .models import Perrito

from django.views.generic import ListView

def galeria(request):
    mostrar=Perrito.objects.filter(estado=1)
    return render (request, 'core/galeria.html', {'doggy': mostrar})

def home(request):
    mostrar=Perrito.objects.filter(estado=2)
    return render (request, 'core/home.html', {'doggy': mostrar})

def adoptados(request):
    if request.method == "POST":
        form = PerritoForm(request.POST, request.FILES)
        if form.is_valid():
            Perrito = form.save(commit=True)
            Perrito.save()
            return redirect('thanks')
    else:
        form = PerritoForm()
    return render(request, 'core/adoptados.html', {'form': form})

def editar(request, id):
    perrito =  get_object_or_404(Perrito,id=id)
    form = PerritoForm(request.POST or None, instance = perrito)
    if form.is_valid():
        form.save()
        return redirect('thanks')
    else:
        form = PerritoForm(request.POST or None, instance = perrito)
    return render(request, 'core/editar.html', {'form': form, 'perrito':perrito})

def listar(request):
    mostrar=Perrito.objects.all()
    return render (request, 'core/listar.html', {'doggy': mostrar})