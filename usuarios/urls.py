from django.urls import path
from .views import registro, iniciar_sesion

urlpatterns = [
    path('register/', registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
]

