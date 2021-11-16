from django.shortcuts import redirect, get_object_or_404, render, get_list_or_404
from django.utils import timezone
from .models import Publicacion
from .forms import PublicacionForm

def publicacion_lista(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'misitio/publicacion_lista.html', {'publicaciones':publicaciones})

def publicacion_detalle(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'misitio/publicacion_detalle.html', {'publicacion':publicacion})

def publicacion_nueva(request):
    if request.method == "POST":
        formulario = PublicacionForm(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('publicacion_detalle', pk=publicacion.pk)
    else:
        formulario = PublicacionForm()
    return render(request, 'misitio/publicacion_editar.html', {'formulario': formulario})

def publicacion_editar(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        formulario = PublicacionForm(request.POST, instance=publicacion)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('publicacion_detalle', pk=publicacion.pk)
    else:
        formulario = PublicacionForm(instance=publicacion)    
    return render(request, 'misitio/publicacion_editar.html', {'formulario': formulario})

def publicacion_borrador_lista(request):
    publicaciones = Publicacion.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'misitio/publicacion_borrador_lista.html', {'publicaciones':publicaciones})

def publicacion_publicar(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    publicacion.publicar()
    return redirect('publicacion_detalle', pk=pk)

def publicacion_eliminar(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    publicacion.delete()
    return redirect('publicacion_lista')