from django.shortcuts import render
from diccionario.models import trastorno 
import random

# Create your views here.
def game(request):
    return render(request, 'game.html')

def obtenerTrastornoAleatorio(request):
    trastornoAleatorio = trastorno.objects.filter(seleccionada=False).order_by("?").first()

    if trastorno:
        trastornoAleatorio.seleccionada = True
        trastornoAleatorio.save()
        Trastorno = trastornoAleatorio.nombre
    else:
        trastorno.objects.update(seleccionada=False)

    return render(request, 'game.html', {'Trastorno': Trastorno})