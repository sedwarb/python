from django.shortcuts import render
from .models import Directores,Peliculas

def index(request):
    peliculas = Peliculas.objects.all()
    lista = list(peliculas)
    return render(
        request,
        'index.html',
        context={'peliculas':lista}
    )
