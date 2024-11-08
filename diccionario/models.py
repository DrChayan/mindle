from django.db import models

# Create your models here.
class trastorno(models.Model):
    nombre=models.CharField(max_length=200)
    contexto=models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class sintomas(models.Model):
    trastorno=models.ForeignKey('trastorno', on_delete=models.CASCADE, default=0)
    sintoma1=models.CharField(max_length=100)
    sintoma2=models.CharField(max_length=100)
    sintoma3=models.CharField(max_length=100)
    sintoma4=models.CharField(max_length=100)
    sintoma5=models.CharField(max_length=100)


