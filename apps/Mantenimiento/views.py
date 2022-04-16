from django.shortcuts import render,redirect
from apps.Inventario.models import Elemento
from .models import Mantenimiento as mantenimientoModel
from django.views.generic import View,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .forms import mantenimientoForm,CierreCasoForm
from datetime import datetime as dt
from apps.Gestion.models import DetallesAsignacion as DetalleModel
# Create your views here.

class ElementoList(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required=['Inventario.view_elemento','Mantenimiento.view_mantenimiento']
	def get(self,request,**kwargs):
		context = {
		'query':Elemento.objects.all(),
		}
		return render (request,'Gestion/Mantenimiento/index.html',context)

class MantenimientoDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Mantenimiento.view_mantenimiento'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		context = {
		'query':mantenimientoModel.objects.filter(elemento_id=ide),
		'obj':Elemento.objects.get(placa=ide)
		}
		return render(request,'Gestion/Mantenimiento/details.html',context)

class Mantenimiento(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url="/auth/login"
	permission_required='Mantenimiento.add_mantenimiento'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']		
		context = {
		'query':Elemento.objects.get(placa=ide),
		'form':mantenimientoForm,
		}
		return render (request,'Gestion/Mantenimiento/create.html',context)
	def post(self,request,**kwargs):
		ide = self.kwargs['pk']
		form = mantenimientoForm(request.POST)
		if form.is_valid():
			detalle = form.cleaned_data['descripcion']
			queryset = Elemento.objects.get(placa=ide)
			mantenimientoModel.objects.create(elemento_id=queryset.placa,user=request.user.username,descripcion=detalle)
			queryset.estado = 'En mantenimiento'
			queryset.save()
			return redirect('mantenimiento:mantenimientoDetails',str(queryset.placa))

class DetalleCaso(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Mantenimiento.view_mantenimiento'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		context = {
		'query':mantenimientoModel.objects.get(PID=ide),
		}
		return render(request,'Gestion/Mantenimiento/mantenimiento.html',context)

class CerrarCaso(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Mantenimiento.change_mantenimiento'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']		
		context = {
		'query':mantenimientoModel.objects.get(PID=ide),
		'form':CierreCasoForm,
		}
		return render (request, 'Gestion/Mantenimiento/cerrarCaso.html',context)
	def post(self,request,**kwargs):
		ide = self.kwargs['pk']
		form = CierreCasoForm(request.POST)
		if form.is_valid():
			irr = form.cleaned_data['irreparable']
			obs = form.cleaned_data['observaciones']
			if not irr:
				q = mantenimientoModel.objects.get(PID=ide)
				q.estado = "Finalizado"
				q.fechaFin = dt.now()
				q.observaciones = obs
				q.save()
				e = Elemento.objects.get(placa=q.elemento_id)
				queryset = DetalleModel.objects.filter(elemento_id = e.placa)
				if queryset:
					e.estado = 'Activo'
					e.save()
				else:
					e.estado = 'Por Asignar'
					e.save()
				return redirect('mantenimiento:mantenimientoRecord',str(ide))
			else:
				q = mantenimientoModel.objects.get(PID=ide)
				row = mantenimientoModel.objects.filter(elemento=q.elemento,estado="En Progreso")
				for element in row:
					a =mantenimientoModel.objects.get(PID = element.PID)
					a.estado="Irreparable"
					a.fechaFin=dt.now()
					a.observaciones=obs
					a.save()
				
				e = Elemento.objects.get(placa=q.elemento_id)
				e.estado = "En Proceso de Baja"
				e.save()
				return redirect('mantenimiento:mantenimientoRecord',str(ide))
