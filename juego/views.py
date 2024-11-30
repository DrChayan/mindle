from django.shortcuts import render
from diccionario.models import trastorno 
import random
from mindle.forms import trastornoForm
from django.utils import timezone

# Create your views here.

def game(request):
    return render(request, 'game.html')

def obtenerTrastorno(request):
    hoy = timezone.now().date()

    trastornoEscogido = trastorno.objects.filter(fecha=hoy).order_by("?").first()

    if trastornoEscogido:
        return str(trastornoEscogido)
    else:
        return "None"
def compararPalabra(request):
    resultado= ""
    trastornoCorrecto = obtenerTrastorno(request)
    
    if request.method == "POST":
        form = trastornoForm(request.POST)
        if form.is_valid():
            inputTrastorno = form.cleaned_data["inputTrastorno"]
            if inputTrastorno.strip() == trastornoCorrecto.strip():
                resultado = "Ganaste trsatornado !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            else:
                resultado = "mmmmm estuvistes cercas xdddd creo"
    else:
        form = trastornoForm()

    return render(request, 'compararPalabra.html',{'form':form, 'resultado': resultado})