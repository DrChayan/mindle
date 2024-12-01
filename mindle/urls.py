"""
URL configuration for mindle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from menu import views as templateMenu
from diccionario import views as templateDiccionario
from juego import views as templateGame
from diccionario.views import diccionario_view
from usuarios import u_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', templateMenu.index, name='index'),
    path('diccionario/', templateDiccionario.diccionario_view, name='diccionario'),  # Usamos la vista 'diccionario_view'
    path('game/', templateGame.game),
    path('prueba/', templateDiccionario.trastorno_list),
    path('usuarios/', include('usuarios.u_urls')),
    path('register/', u_views.registro, name='registro'),
]
