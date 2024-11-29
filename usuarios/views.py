from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            #iniciar_sesion(request, user) ver si se pued einiciar s al registrarse automaticamente
            return redirect('game')  # Redirige a la página principal (asegúrate de que esta URL exista)
    else:
        form=RegistroForm()
    return render(request, 'registrarse.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicioDeSesion.html')  # Redirige al inicio (verifica que la ruta 'inicio' exista)
    else:
        form = AuthenticationForm()
    return render(request, 'inicioDeSesion.html', {'form': form})
