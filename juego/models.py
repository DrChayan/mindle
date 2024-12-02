from django.db import models
from django.contrib.auth.models import User

class Puntaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.usuario.username}: {self.puntaje}"