from django.db import models
from apps.Inventario.models import Elemento
# Create your models here.
class Baja(models.Model):
	PID = models.AutoField(primary_key=True)
	user = models.CharField(max_length=10)
	timestamps = models.DateTimeField(auto_now=True)
	def __str__(self):
		return '%s'%(self.PID)

class DetalleBaja(models.Model):
	baja = models.ForeignKey(Baja,on_delete=models.CASCADE)
	elemento = models.ForeignKey(Elemento,on_delete=models.CASCADE)
	autorizado = models.BooleanField(default=True)
	timestamps = models.DateTimeField(auto_now=True)
	def __str__(self):
			return '%s %s'%(self.baja,self.elemento)
