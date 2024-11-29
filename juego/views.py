from django.shortcuts import render
from diccionario.models import trastorno 
import random
from mindle.forms import trastornoForm

# Create your views here.

def game(request):
    return render(request, 'game.html')

def obtenerTrastornoAleatorio(request):

    trastornoAleatorio = trastorno.objects.filter(seleccionada=False).order_by("?").first()

    if trastornoAleatorio:
        trastornoAleatorio.seleccionada = True
        trastornoAleatorio.save()
        Trastorno = trastornoAleatorio.nombre
    else:
        actualizar(request)

    return str(trastornoAleatorio)

def actualizar(request):
    trastorno.objects.filter(seleccionada=True).update(seleccionada=False)
    
    return 0
def compararPalabra(request):
    resultado= ""
    trastornoCorrecto = obtenerTrastornoAleatorio(request)
    
    if request.method == "POST":
        form = trastornoForm(request.POST)
        if form.is_valid():
            inputTrastorno = form.cleaned_data["inputTrastorno"]
            if inputTrastorno.strip() == trastornoCorrecto.strip():
                resultado = "Ganaste trsatornado !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            else:
                resultado = trastornoCorrecto
    else:
        form = trastornoForm()

    return render(request, 'compararPalabra.html',{'form':form, 'resultado': resultado})