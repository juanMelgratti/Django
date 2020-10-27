from django.db import models
from usuarios import Usuarios

class Producto(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20)
    cantidad = models.IntegerField(default=0)
    descuento = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.OneToOneField(Usuarios, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ProductoEnCarrito')

class ProductoEnCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)



