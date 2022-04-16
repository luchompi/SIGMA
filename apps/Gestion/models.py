from django.db import models
from apps.Personas.models import Funcionario
from apps.Inventario.models import Elemento

class Asignacion(models.Model):
	funcionario =models.ForeignKey(Funcionario, on_delete=models.CASCADE)
	user = models.CharField(max_length=50)
	timestamps = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name = "Asignacion"
		verbose_name_plural = "Asignaciones"
	def __str__(self):
		return '%s %s'%(self.funcionario,self.user)

class DetallesAsignacion(models.Model):
	asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE)
	elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)
	timestamps = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name = "DetallesAsignacion"
		verbose_name_plural = "DetallesAsignaciones"
	def __str__(self):
		return '%s %s'%(self.asignacion,self.elemento)
