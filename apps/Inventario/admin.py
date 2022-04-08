from django.contrib import admin
from .models import Marca,Modelo,Elemento
# Register your models here.
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Elemento)