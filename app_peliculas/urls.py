from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_peliculas, name='lista_peliculas'),
    path('consultar/', views.consultar_pelicula, name='consultar_pelicula'),
]