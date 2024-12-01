from django.shortcuts import render, redirect
from diccionario.models import trastorno, sintomas
import random
from mindle.forms import trastornoForm
from django.utils import timezone

# Create your views here.

def ganar(request):
    if request.session.get('acierto', True): 
        return redirect('juego')
        return redirect('index')
    else:
        return redirect('juego')

def obtenerTrastorno(request):
    hoy = timezone.now().date()

    trastornoEscogido = trastorno.objects.filter(fecha=hoy).order_by("?").first()

    if trastornoEscogido:
        return trastornoEscogido
    else:
        return "None"

def reiniciar(trastorno):
    pass
def obtener_sintomas(trastorno_obj):
    # Filtrar los síntomas que corresponden a este trastorno específico
    
    try:
        trastorno_id = trastorno.objects.get(nombre=trastorno_obj)
    except:
        return []
    sintomas_objetos = sintomas.objects.filter(id=trastorno_id.id)

    # Crear una lista de los síntomas (siendo cada síntoma un string)
    sintomas_lista = []

    # Recorremos los objetos de síntomas y los agregamos a la lista
    for sintomas_obj in sintomas_objetos:
        sintomas_lista.append(sintomas_obj.sintoma1)
        sintomas_lista.append(sintomas_obj.sintoma2)
        sintomas_lista.append(sintomas_obj.sintoma3)
        sintomas_lista.append(sintomas_obj.sintoma4)
        sintomas_lista.append(sintomas_obj.sintoma5)

    # Filtramos la lista para eliminar valores vacíos o None
    sintomas_lista = [sintoma for sintoma in sintomas_lista if sintoma]  # Elimina valores vacíos o None
    print(sintomas_lista)
    return sintomas_lista  # Devuelve los síntomas como lista de strings

def comparar_sintomas(sintomas_correctos, sintomas_usuario):
    sintomas_comunes = list(set(sintomas_correctos) & set(sintomas_usuario))
    print(sintomas_comunes)
    return sintomas_comunes

def compararPalabra(request):
    resultado= ""
    trastornoCorrecto = str(obtenerTrastorno(request))
    print(type(request.session.get('acierto', False)))
    mostrar_modal = False
    if 'intentos' not in request.session:
        request.session['intentos'] = 0
    if request.method == "POST":
        form = trastornoForm(request.POST)
        if form.is_valid():
            request.session['intentos'] += 1
            request.session.modified = True
            inputTrastorno = form.cleaned_data["inputTrastorno"]
            if inputTrastorno.strip() == trastornoCorrecto.strip():
                mostrar_modal = True
                request.session['acierto'] = True
            else:
                resultado = comparar_sintomas(obtener_sintomas(inputTrastorno),obtener_sintomas(trastornoCorrecto))
                request.session['acierto'] = False
                print(resultado)
    else:
        form = trastornoForm()

    return render(request, 'game.html',{'form':form, 'resultado': resultado, 'mostrar_modal': mostrar_modal, 'intentos': request.session['intentos']})