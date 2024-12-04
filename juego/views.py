from django.shortcuts import render, redirect
from diccionario.models import trastorno, sintomas
import random
from mindle.forms import trastornoForm
from django.utils import timezone
from .models import Puntaje

# Create your views here.

def ganar(request):
    if request.session.get('acierto', True): 
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
    trastorno_n = trastorno.objects.filter(nombre__iexact=trastorno_obj)
    if trastorno_n.exists():
        trastorno_id = trastorno_n.first()
    else:
        print("No se encontró el trastorno.")
    #try:
    #    trastorno_id = trastorno.objects.get(nombre=trastorno_obj)
    #except:
    #    return []
    sintomas_objetos = sintomas.objects.filter(trastorno_id=trastorno_id.id)

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
    print(sintomas_lista, trastorno_id.id)
    return sintomas_lista  # Devuelve los síntomas como lista de strings

def comparar_sintomas(sintomas_correctos, sintomas_usuario):
    sintomas_comunes = list(set(sintomas_correctos) & set(sintomas_usuario))
    print(sintomas_comunes, "comun")
    return sintomas_comunes

def obtenerContexto(trastorno_obj):
    Trastorno = trastorno.objects.get(nombre=trastorno_obj)
    contexto = Trastorno.contexto
    return contexto

def compararPalabra(request):
    resultado= ""
    trastornoCorrecto = str(obtenerTrastorno(request))
    
    trastornoCorrecto = trastornoCorrecto.lower()
    print(trastornoCorrecto, "correcto")
    print(type(request.session.get('acierto', False)))
    mostrar_modal = False
    if 'intentos' not in request.session:
        request.session['intentos'] = 0
    if request.method == "POST":
        form = trastornoForm(request.POST)
        if form.is_valid():
            request.session['intentos'] += 1
            request.session.modified = True
            inputTrastorno =form.cleaned_data["inputTrastorno"]
            print(inputTrastorno)
            if str(inputTrastorno).strip().lower() == trastornoCorrecto.lower().strip():
                mostrar_modal = True
                request.session['acierto'] = True
                if request.user.is_authenticated:  # Solo si el jugador está logueado
                    # Asegúrate de que el usuario tiene un puntaje registrado
                    puntaje_usuario, created = Puntaje.objects.get_or_create(usuario=request.user)
                    puntaje_usuario.puntaje += 1  # Sumar un punto por acertar
                    puntaje_usuario.save()  # Guardar el puntaje actualizado
            else:
                resultado = comparar_sintomas(obtener_sintomas(inputTrastorno),obtener_sintomas(trastornoCorrecto))
                request.session['acierto'] = False
                print(resultado)
    else:
        form = trastornoForm()

    return render(request, 'game.html',
        {'form':form, 
        'resultado': resultado, 
        'mostrar_modal': mostrar_modal, 
        'intentos': request.session['intentos'],
        'cTrastorno': trastornoCorrecto,
        'dTrastorno': obtenerContexto(obtenerTrastorno(request))}
        )