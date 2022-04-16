from django.db import models
from apps.Inventario.models import Elemento
# Create your models here.
class Mantenimiento(models.Model):
	PID = models.AutoField(primary_key=True)
	elemento = models.ForeignKey(Elemento,on_delete=models.CASCADE)
	user = models.CharField(max_length=50)
	fechaFin=models.DateTimeField(null=True,blank=True)
	descripcion = models.CharField(max_length=50000)
	observaciones = models.CharField(max_length=50000)
	timestamps = models.DateTimeField(auto_now=True)
	estado = models.CharField(max_length=100,default="En Progreso")
	def __str__(self):
		return '%s %s'%(self.PID,self.elemento)    