from django.contrib import admin

from .models import Producto
from .models import Carrito



admin.site.register(Producto)
admin.site.register(Carrito)

