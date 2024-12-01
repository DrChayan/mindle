# diccionario/apps.py
from django.apps import AppConfig

class DiccionarioConfig(AppConfig):
    name = 'diccionario'

    def ready(self):
        # No es necesario importar modelos aquí
        # Si necesitas importar algo aquí, asegúrate de que no sea una operación que dependa de los modelos directamente
        pass
