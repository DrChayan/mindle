from django.shortcuts import render
from juego.models import Puntaje

# Create your views here.
def index(request):
        # Obtener el ranking de los 10 jugadores con mayor puntaje
    ranking = Puntaje.objects.all().order_by('-puntaje')[:5]

    return render(request, 'index.html', {'user': request.user, 'ranking': ranking})


def login(request):
    return render(request, 'inicioDeSesion.html')

def register(request):
    return render(request, 'registrarse.html')