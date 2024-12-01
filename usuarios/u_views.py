from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def registro(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #iniciar_sesion(request, user) ver si se pued einiciar s al registrarse automaticamente
            return redirect('/')  # Redirige a la página principal (asegúrate de que esta URL exista)
    else:
        form=RegistroForm()
    return render(request, 'registrarse.html', {'form': form})

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirige al inicio (verifica que la ruta 'inicio' exista)
    else:
        form = AuthenticationForm()
    return render(request, 'inicioDeSesion.html', {'form': form})

@login_required 
def perfil(request):
    return render(request, 'usuarios/perfil.html')
               
def cerrar_sesion (request) :
    if request.user.is_authenticated:
        logout (request)
    return redirect ('/')

def index (request):
    return render (request, 'index.htmI', {'user': request.user})