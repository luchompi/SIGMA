from cmath import log
from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView,UpdateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from apps.Inventario.models import Elemento
from .models import Asignacion,DetallesAsignacion as DetalleModel
from apps.Personas.models import Funcionario
from .sessions import Asignacion as asig

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

class Func2Session(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Gestion.view_asignacion'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		if ide:
			context={
			'query':Elemento.objects.filter(estado='Por Asignar'),
			'funcionario':Funcionario.objects.get(identificacion=ide),
			}
			return render(request,'Gestion/Asignacion/asignacion.html',context)

class add2Session(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Gestion.add_asignacion'
	def get(self,request, **kwargs):
		aux = self.kwargs['iden']
		ide = self.kwargs['pk']
		obj = Elemento.objects.get(placa=ide)
		if obj:
			func = asig(self.request)
			func.add(obj)
			return redirect('gestion:func2Session',str(aux))

class del2Session(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Gestion.add_asignacion'
	def get(self,request, **kwargs):
		aux = self.kwargs['iden']
		ide = self.kwargs['pk']
		obj = Elemento.objects.get(placa=ide)
		if obj:
			func = asig(self.request)
			func.remove(obj)
			return redirect('gestion:func2Session',str(aux))

class cancel(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Gestion.add_asignacion'
	def get(self,request, **kwargs):
		ide = self.kwargs['iden']
		func = asig(self.request)
		func.clear()
		return redirect('gestion:funcAsigDetail',str(ide))

class successAsignacion(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Gestion.add_asignacion'
	def get(self,request, **kwargs):
		ide = self.kwargs['iden']
		Asignacion.objects.create(funcionario_id=ide,user=request.user.username)
		req = Asignacion.objects.filter(funcionario_id=ide,user=request.user.username).latest('timestamps')
		func = asig(self.request)
		obj = request.session["asignacion"]
		for row in obj.keys():
			element = obj[row]["elemento_id"]
			DetalleModel.objects.create(asignacion_id=req.id,elemento_id=element)
			a = Elemento.objects.get(placa=element)
			a.estado='Activo'
			a.save()
		func.clear()
		return redirect('gestion:AsigQuery',str(req.id))

class AsigQuery(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Gestion.view_asignacion'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		context={
		'query':Asignacion.objects.get(id=ide),
		'object_list':DetalleModel.objects.filter(asignacion=ide),
		}
		return render(request,'Gestion/Asignacion/AsigDetail.html',context)