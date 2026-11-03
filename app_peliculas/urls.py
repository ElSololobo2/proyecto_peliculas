from django.urls import path
from . import views

urlpatterns = [

    # Mostrar el catálogo y gestionar el registro y edición.
    path('', views.lista_peliculas, name='lista_peliculas'),

    # Consultar una película mediante su ID.
    path('consultar/', views.consultar_pelicula, name='consultar_pelicula'),

    # Eliminar una película mediante su ID.
    path('eliminar/<int:pelicula_id>/', views.eliminar_pelicula, name='eliminar_pelicula'),

]