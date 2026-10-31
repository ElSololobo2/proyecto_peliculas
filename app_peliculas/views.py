from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Pelicula

def lista_peliculas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        genero = request.POST.get('genero')
        comentarios = request.POST.get('comentarios')
        proveedor = request.POST.get('Proveedor') or 0
        cantidad = request.POST.get('cantidad') or 0
        estado = request.POST.get('estado') or 'Disponible'
        precio_renta = request.POST.get('precio_renta') or 0        

        if titulo:
            Pelicula.objects.create(titulo=titulo, genero=genero, comentarios=comentarios, proveedor = int (proveedor), cantidad=int(cantidad), estado =estado, precio_renta= int(precio_renta))
        return redirect('lista_peliculas')

    peliculas = Pelicula.objects.all()
    return render(request, 'app_peliculas/lista_peliculas.html', {'peliculas': peliculas})

def consultar_pelicula(request):
    id_pelicula = request.GET.get('id')

    try:
        pelicula = Pelicula.objects.get(id=id_pelicula)

        return JsonResponse({
            'encontrada': True,
            'id': pelicula.id,
            'titulo': pelicula.titulo,
            'genero': pelicula.genero,
            'comentarios': pelicula.comentarios,
            'proveedor': pelicula.proveedor,
            'cantidad': pelicula.cantidad,
            'estado': pelicula.estado,
            'precio_renta': pelicula.precio_renta
        })

    except (Pelicula.DoesNotExist, ValueError, TypeError):
        return JsonResponse({
            'encontrada': False,
            'mensaje': 'No se encontró ninguna película con ese ID.'
        })
