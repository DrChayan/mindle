import os, django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mindle.settings")
django.setup()

from  juego.views import obtenerTrastornoAleatorio

obtenerTrastornoAleatorio(None)