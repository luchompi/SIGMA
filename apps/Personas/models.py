from django.db import models
from apps.Empresa.models import SedeDependencia
# Create your models here.
class Funcionario(models.Model):
    identificacion= models.IntegerField(primary_key=True,verbose_name='Identificacion de Funcionario',unique=True,error_messages={'unique':'Ya está registrado esta Identificación'})
    nombres = models.CharField(max_length=100, verbose_name='Nombres del Funcionario')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos del Funcionario')
    direccion = models.CharField(max_length=100, verbose_name='Direccion de residencia')
    telefono = models.CharField(max_length=100, verbose_name='Teléfono de Contacto')
    correo = models.EmailField(verbose_name='Correo electronico')
    sede = models.ForeignKey(SedeDependencia, on_delete=models.SET_NULL,null=True, verbose_name='Sede a la la que está adscrito')
    timestamps=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
    def __str__(self):
        return '%s %s %s'%(self.identificacion,self.nombres,self.apellidos)

class Proveedor(models.Model):
    NIT=models.CharField(max_length=50,primary_key=True,verbose_name="NIT/RUT de proveedor",unique=True,error_messages={'unique':'Ya está registrado esta identificacion'})
    razonSocial=models.CharField(max_length=100,verbose_name="Nombre/Razón Social de Proveedor")
    direccion=models.CharField(max_length=100,verbose_name="Dirección de la empresa")
    dir_venta=models.CharField(max_length=100,verbose_name="Dirección de Punto de Venta (Si hubiere)",null=True,blank=True)
    telefono1=models.CharField(max_length=20,verbose_name="Telefono de Contacto")
    telefono2=models.CharField(max_length=20,verbose_name="Telefono de contacto Segundario (Si hubiere)",null=True,blank=True)
    correo=models.EmailField(verbose_name="Correo electronico de contacto (Si hubiere)",null=True,blank=True)
    vendedor=models.CharField(max_length=100,verbose_name="Nombre de contacto con la entidad/persona",null=True,blank=True)
    tel_vendedor=models.CharField(max_length=10,verbose_name="Telefono de vendedor",null=True,blank=True)
    timestamps=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    def __str__(self):
        return '%s %s'%(self.NIT,self.razonSocial)
