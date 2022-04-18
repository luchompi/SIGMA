from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import View
from .models import Baja, DetalleBaja as DetalleModel
from apps.Inventario.models import Elemento
from datetime import datetime as dt,date as d, timedelta
from .sessions import baja
# Create your views here.
class BajaIndex(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Bajas.view_baja'
	def get(self,request,**kwargs):
		context = {
		'query':Elemento.objects.filter(estado="En Proceso de Baja",autorizado = False)
		}
		return render(request,'Gestion/Baja/index.html',context)

class add(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Bajas.add_baja'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		b = baja(self.request)
		obj = Elemento.objects.get(placa=ide)
		b.add(obj)
		return redirect('bajas:BajaIndex')

class remove(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Bajas.view_baja'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		b =baja(self.request)
		obj = Elemento.objects.get(placa = ide)
		print("entrando a borrar")
		b.remove(obj)
		return redirect('bajas:BajaIndex')

class cls(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url = '/auth/login/'
	permission_required = 'Bajas.view_baja'
	def get(self,request,**kwargs):
		b = baja(self.request)
		b.clear()
		return redirect('bajas:BajaIndex')

class done(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Bajas.add_baja'
	def get(self,request,**kwargs):
		obj = request.session["baja"]
		b = baja(self.request)
		Baja.objects.create(user=request.user)
		q = Baja.objects.filter(user=request.user).latest('timestamps')
		for row in obj.keys():
			placa=obj[row]["placa"]
			a = d.today()
			date = a + timedelta(days=15)
			print(date)
			c =Elemento.objects.get(placa=placa)
			c.autorizado = True
			c.save()
			DetalleModel.objects.create(elemento_id=placa,baja=q,fechaBorrado=date)
		b.clear()
		return redirect('bajas:BajaIndex')

class index(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Bajas.view_baja'
	def get(self,request,**kwargs):
		context = {
		'query':Baja.objects.all(),
		}
		return render(request,'Gestion/Baja/list.html',context)

class detail(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Bajas.view_baja'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		context = {
		'object':Baja.objects.get(PID=ide),
		'query':DetalleModel.objects.filter(baja=ide),
		}
		return render(request,'Gestion/Baja/detail.html',context)