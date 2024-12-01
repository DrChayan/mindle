from django.urls import path
from .u_views import registro, iniciar_sesion, perfil, cerrar_sesion
from . import u_views

urlpatterns = [
    path('register/', u_views.registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('perfil/', perfil, name='perfil'),
    path('logout/', cerrar_sesion, name='logout'),
]

