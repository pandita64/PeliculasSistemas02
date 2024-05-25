from django.shortcuts import render
from django.http import HttpResponse
from . import models 

# Create your views here.
def cinePeliculas(request):
    mensaje = models.Mensaje.objects.first()
    pelicula = models.pelicula.objects.all()
    datos={
        'mensaje' :mensaje,
        'peliculas' :pelicula
    }
    #print(pelicula)
    return render(request, 'index.html',datos)




