from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import trastorno
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
    return render(request, 'diccionarioprueba.html', {'trastornos': trastornos, 'query': query})

def trastorno_detail(request, item_id):
    item = get_object_or_404(trastorno, id=item_id)  # Obtén un único ítem
    return render(request, 'trastorno.html', {'trastorno': trastorno}) 

def diccionario_view(request):
    query = request.GET.get('q', '')  # Obtiene el valor de la consulta de la URL
    if query:
        trastornos = trastorno.objects.filter(nombre__icontains=query).order_by('nombre')  # Filtra los trastornos que coinciden con la consulta
    else:
        trastornos = trastorno.objects.all().order_by('nombre')  # Si no hay consulta, devuelve todos los trastornos

    return render(request, 'diccionarioprueba.html', {'trastornos': trastornos, 'query': query})