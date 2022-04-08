from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import View,CreateView,UpdateView,DeleteView,ListView
from .models import Funcionario,Proveedor
from .forms import funcionarioForm,proveedorForm
from .utils import render_to_pdf
from django.http import HttpResponse
from datetime import datetime as dt

class FuncionarioListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
	login_url='/auth/login'
	permission_required='Personas.view_funcionario'
	model = Funcionario
	template_name = "Personas/Funcionario/index.html"

class FuncionarioCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
	login_url='/auth/login'
	permission_required='Personas.add_funcionario'
	model = Funcionario
	form = funcionarioForm
	fields=['identificacion','nombres','apellidos','direccion','telefono','correo','sede']
	template_name="Personas/Funcionario/create.html"
	success_url='/personas/funcionarios'

class FuncionarioUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
	login_url='/auth/login'
	permission_required='Personas.change_funcionario'
	model = Funcionario
	form = funcionarioForm
	fields=['nombres','apellidos','direccion','telefono','correo','sede']
	template_name = "Personas/Funcionario/update.html"
	success_url='/personas/funcionarios/detalles/{identificacion}'

class FuncionarioDeleteView(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Personas.delete_funcionario'
	def get(self,request,**kwargs):
		ide=self.kwargs['pk']
		Funcionario.objects.get(identificacion=ide).delete()
		return redirect('personas:funcIndex')

class PDF(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Personas.view_funcionario'
    def get(self,request,*args,**kwargs):
    	ide = self.kwargs['pk']
    	context = {'query': Funcionario.objects.get(identificacion=ide),'timestamps':dt.now(),'usuario':request.user,}
    	pdf = render_to_pdf('Personas/Funcionario/pdf.html', context)
    	return HttpResponse(pdf, content_type='application/pdf')

class ProveedorListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
	login_url='/auth/login'
	permission_required='Personas.add_proveedor'
	model = Proveedor
	template_name="Personas/Proveedor/index.html"

class ProveedorCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
	login_url='/auth/login'
	permission_required='Personas.add_proveedor'
	model = Proveedor
	form = proveedorForm
	fields = ['NIT','razonSocial','direccion','dir_venta','telefono1','telefono2','correo','vendedor','tel_vendedor']
	template_name = "Personas/Proveedor/create.html"
	success_url='/personas/proveedores'
	def form_valid(self,form):
		NIT = form.cleaned_data['NIT']
		form.save()
		return redirect('personas:proovUpdate',str(NIT))

class ProveedorUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
	login_url='/auth/login'
	permission_required='Personas.change_proveedor'
	model = Proveedor
	form = proveedorForm
	fields = ['NIT','razonSocial','direccion','dir_venta','telefono1','telefono2','correo','vendedor','tel_vendedor']
	template_name = "Personas/Proveedor/update.html"
	success_url='/personas/proveedores/detalles/{NIT}'

class ProveedorDeleteView(LoginRequiredMixin,PermissionRequiredMixin,View):
	login_url='/auth/login'
	permission_required='Personas.delete_funcionario'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		Proveedor.objects.get(NIT=ide).delete()
		return redirect('personas:proovIndex')