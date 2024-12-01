from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'user': request.user})

def login(request):
    return render(request, 'inicioDeSesion.html')

def register(request):
    return render(request, 'registrarse.html')