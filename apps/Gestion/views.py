from datetime import datetime as dt
from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView,UpdateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from apps.Inventario.models import Elemento
from .models import Asignacion,DetallesAsignacion as DetalleModel
from apps.Personas.models import Funcionario
from .sessions import Asignacion as asig
from .utils import render_to_pdf
from django.http import HttpResponse
from .forms import traspasos


#Operaciones de Asignacion
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

class PDF(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Gestion.view_asignacion'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		data = self.kwargs['iden']
		query = Asignacion.objects.get(id=ide),
		context = {
		'query': query,
		'funcionario':Funcionario.objects.get(identificacion=data),
		'elementos':DetalleModel.objects.filter(asignacion_id=ide),
		'timestamps':dt.now(),
		'titulo':"Reporte de Asignacion con PID: "+ide,
		'cuerpo':"De conformidad a lo consultado en los reportes del sistema de asginaciones, la oficina de sistemas reporta que en su haber, los siguientes elementos se encuentran asignados bajo las siguientes condiciones",
		'noticia':"Esta notificacion se realiza con el proposito de informarle acerca de los elementos que usted tiene a su cargo, y por ende, establecer que en caso de presentarse alguna novedad con el elemento, usted se hace responsable sobre la perdida o robo del mismo, siempre y cuando se realice el respectivo denuncio sobre el mismo o, en caso contraro, que sistemas sea consciente sobre dicha novedad.",
		'user':request.user.username,}
		pdf = render_to_pdf('Gestion/Asignacion/PDF.html', context)
		return HttpResponse(pdf, content_type='application/pdf')

#Operaciones de Traspasos
class TraspasoIndex(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Gestion.view_traspaso'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		q = DetalleModel.objects.get(elemento_id = ide)
		context = {
		'elemento': Elemento.objects.get(placa = ide),
		'form':traspasos,
		'detalle':q,
		}
		return render(request,'Gestion/Traspaso/index.html',context)
	def post(self,request,**kwargs):
		form=traspasos(request.POST)
		ide =self.kwargs['pk']
		q = self.kwargs['pid']
		if form.is_valid():
			Asignacion.objects.create(funcionario=form.cleaned_data['funcionario'],user=request.user.username)
			retrive = Asignacion.objects.latest('timestamps')
			q = DetalleModel.objects.get(elemento_id=ide)
			row =DetalleModel.objects.get(elemento_id=ide)
			aux = q.asignacion_id
			row.asignacion_id = retrive.id
			row.save()
			if DetalleModel.objects.filter(asignacion_id=aux).count() == 0:	
				Asignacion.objects.get(id=q).delete()
			return redirect('gestion:AsigQuery',str(row.asignacion_id))			
	
