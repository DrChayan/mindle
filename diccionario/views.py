from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import trastorno, sintomas
# Create your views here.
def pagDicc(request):
    return render(request, 'diccionarioprueba.html')


def trastorno_list(request):
    query = request.GET.get('q', '')  # Obtener el parámetro 'q' de la URL
    if query:
        trastornos = trastorno.objects.filter(nombre__istartswith=query).order_by('nombre')
        # 'nombre__istartswith' filtra los nombres que comienzan con 'query' (sin importar mayúsculas)
    else:
        trastornos = trastorno.objects.all().order_by('nombre')

     # Crear una lista de diccionarios con los trastornos y sus síntomas asociados
    datos_trastornos = []
    for t in trastornos:
        sintomas_asociados = sintomas.objects.filter(trastorno=t)  # Obtén los síntomas del trastorno
        datos_trastornos.append({
            'trastorno': t,
            'sintomas': [
                sintomas_asociados.first().sintoma1, 
                sintomas_asociados.first().sintoma2,
                sintomas_asociados.first().sintoma3,
                sintomas_asociados.first().sintoma4,
                sintomas_asociados.first().sintoma5
            ] if sintomas_asociados.exists() else []  # Verifica si hay síntomas
        })

    return render(request, 'diccionarioprueba.html', {'datos_trastornos': datos_trastornos, 'query': query})

def trastorno_detail(request, item_id):
    item = get_object_or_404(trastorno, id=item_id)  # Obtén un único ítem
    return render(request, 'trastorno.html', {'trastorno': trastorno}) 

def diccionario_view(request):
    query = request.GET.get('q', '')  # Obtiene el valor de la consulta de la URL
    if query:
        trastornos = trastorno.objects.filter(nombre__icontains=query).order_by('nombre')  # Filtra los trastornos que coinciden con la consulta
    else:
        trastornos = trastorno.objects.all().order_by('nombre')  # Si no hay consulta, devuelve todos los trastornos
         # Crear una lista de diccionarios con los trastornos y sus síntomas asociados
    datos_trastornos = []
    for t in trastornos:
        sintomas_asociados = sintomas.objects.filter(trastorno=t)  # Obtén los síntomas del trastorno
        datos_trastornos.append({
            'trastorno': t,
            'sintomas': [
                sintomas_asociados.first().sintoma1, 
                sintomas_asociados.first().sintoma2,
                sintomas_asociados.first().sintoma3,
                sintomas_asociados.first().sintoma4,
                sintomas_asociados.first().sintoma5
            ] if sintomas_asociados.exists() else []  # Verifica si hay síntomas
        })

    return render(request, 'diccionarioprueba.html', {'datos_trastornos': datos_trastornos, 'query': query})
