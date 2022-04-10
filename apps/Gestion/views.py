from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Asignacion,DetallesAsignacion as DetalleModel
from apps.Personas.models import Funcionario


class AsignacionListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
	login_url='/auth/login'
	permission_required='Gestion.view_asignacion'
	model = Funcionario
	template_name = "Gestion/Asignacion/index.html"

class AsignacionDetails(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Gestion.view_asignacion'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		context={
		'query':Asignacion.objects.filter(funcionario=ide),
		'funcionario':Funcionario.objects.get(identificacion=ide),
		}
		return render(request,'Gestion/Asignacion/funcDetail.html',context)