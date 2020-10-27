from django.db import models

class Usuarios(models.Model):
    nombre_de_usuario = models.CharField(max_length=40, primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=20)
    email = models.CharField(max_length=250)


