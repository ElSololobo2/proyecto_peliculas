from django.shortcuts import render, redirect
from .models import Pelicula

def lista_peliculas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        genero = request.POST.get('genero')
        comentarios = request.POST.get('comentarios')
        
        if titulo:
            Pelicula.objects.create(titulo=titulo, genero=genero, comentarios=comentarios)
        return redirect('lista_peliculas')

    peliculas = Pelicula.objects.all()
    return render(request, 'app_peliculas/lista_peliculas.html', {'peliculas': peliculas})