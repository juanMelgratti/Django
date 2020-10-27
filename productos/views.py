from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.urls import reverse

from django.utils import timezone

from django.views import generic

from .models import Producto
from .models import Carrito
from .models import ProductoEnCarrito

precio_total_a_apagar = 0

def index(request):

    productos = Producto.objects.all().order_by('descuento')
    return render(request, 'productos/index.html', {'productos':productos})

def search(request, palabra):

    productos_encontrados = Producto.objects.filter(name__contains=palabra)
    return render(request, 'productos/search.html', {'productos_encontrados':productos_encontrados})

def producto(request):

    p = Producto.objects.filter(nombre__exact=request.producto)
    return render(request, 'productos/producto.html', {'producto':p})

def agregar_a_carrito(request):

    carrito, _ = Carrito.objects.get_or_create(usuario=request.usuario)
    producto = Producto.objects.get(nombre=request.nombre)
    producto_en_carrito, _ = ProductoEnCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    producto_en_carrito.cantidad += request.cantidad
    producto_en_carrito.save()
    productos_en_carrito = ProductoEnCarrito.objects.filter(carrito=carrito)
    total = sum((p.producto.precio * p.cantidad) for p in productos_en_carrito)
    return render(request, 'productos/carrito.html', {'total':total})