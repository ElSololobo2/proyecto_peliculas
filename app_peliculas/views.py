
# ==========================================================================
# IMPORTACIONES
# ==========================================================================

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Pelicula


# ==========================================================================
# 1. REGISTRAR Y EDITAR PELÍCULAS (CREATE / UPDATE)
# ==========================================================================

def lista_peliculas(request):

    # Comprobar si se recibió información mediante el formulario.
    if request.method == 'POST':

        # Obtener el ID oculto para identificar si se editará un registro.
        pelicula_id = request.POST.get('pelicula_id')

        # Capturar los datos enviados desde el formulario.
        titulo = request.POST.get('titulo')
        genero = request.POST.get('genero')
        comentarios = request.POST.get('comentarios')
        proveedor = request.POST.get('proveedor') or 0
        cantidad = request.POST.get('cantidad') or 0
        estado = request.POST.get('estado') or 'Disponible'
        precio_renta = request.POST.get('precio_renta') or 0

        # Verificar que se haya proporcionado un título.
        if titulo:

            if pelicula_id:
                # ----------------------------------------------------------
                # EDITAR (UPDATE): Actualizar una película existente.
                # ----------------------------------------------------------

                pelicula = get_object_or_404(Pelicula, id=pelicula_id)

                # Asignar los nuevos valores a los campos del registro.
                pelicula.titulo = titulo
                pelicula.genero = genero
                pelicula.comentarios = comentarios
                pelicula.proveedor = int(proveedor)
                pelicula.cantidad = int(cantidad)
                pelicula.estado = estado
                pelicula.precio_renta = int(precio_renta)

                # Guardar los cambios en la base de datos.
                pelicula.save()

            else:
                # ----------------------------------------------------------
                # REGISTRAR (CREATE): Crear una nueva película.
                # ----------------------------------------------------------

                Pelicula.objects.create(
                    titulo=titulo,
                    genero=genero,
                    comentarios=comentarios,
                    proveedor=int(proveedor),
                    cantidad=int(cantidad),
                    estado=estado,
                    precio_renta=int(precio_renta),
                )

        # Regresar al catálogo después de registrar o editar.
        return redirect('lista_peliculas')

    # Obtener todos los registros de películas.
    peliculas = Pelicula.objects.all()

    # Mostrar el catálogo y enviar la lista de películas al HTML.
    return render(
        request,
        'app_peliculas/lista_peliculas.html',
        {'peliculas': peliculas}
    )


# ==========================================================================
# 2. CONSULTAR PELÍCULAS (READ)
# ==========================================================================

def consultar_pelicula(request):

    # Obtener el ID enviado desde el formulario de consulta.
    id_pelicula = request.GET.get('id')

    try:
        # Buscar la película correspondiente al ID proporcionado.
        pelicula = Pelicula.objects.get(id=id_pelicula)

        # Enviar los datos encontrados en formato JSON.
        return JsonResponse({
            'encontrada': True,
            'id': pelicula.id,
            'titulo': pelicula.titulo,
            'genero': pelicula.genero,
            'comentarios': pelicula.comentarios,
            'proveedor': pelicula.proveedor,
            'cantidad': pelicula.cantidad,
            'estado': pelicula.estado,
            'precio_renta': pelicula.precio_renta,
        })

    except (Pelicula.DoesNotExist, ValueError, TypeError):
        # Informar cuando no se encuentre una película con ese ID.
        return JsonResponse({
            'encontrada': False,
            'mensaje': 'No se encontró ninguna película con ese ID.',
        })


# ==========================================================================
# 3. ELIMINAR PELÍCULAS (DELETE)
# ==========================================================================

@require_POST
def eliminar_pelicula(request, pelicula_id):

    # Buscar la película por su ID; si no existe, devolver error 404.
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)

    # Eliminar el registro seleccionado de la base de datos.
    pelicula.delete()

    # Regresar al catálogo después de completar la eliminación.
    return redirect('lista_peliculas')
