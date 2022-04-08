from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,UpdateView,DeleteView,View
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Sede,Dependencia,SedeDependencia as DetalleModel
from .forms import SedeForm,DependenciaForm
from django.http import HttpResponse
from .session import sede, detalle
# Create your views here.
class SedeCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url='/auth/login'
    permission_required='Empresa.add_sede'
    model=Sede
    fields=['sede']
    form=SedeForm
    template_name='Empresa/Sede/index.html'
    success_url="."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Sede.objects.all()
        return context
    def form_valid(self,form):
        form.save()
        consulta = form.cleaned_data['sede']
        queryset = Sede.objects.get(sede=consulta)
        s = sede(self.request)
        s.add(queryset)
        return redirect('empresa:sedeDep',queryset.id)



class SedeUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='/auth/login'
    permission_required='Empresa.change_sede'
    model=Sede
    fields=['sede']
    form=SedeForm
    template_name='Empresa/Sede/update.html'
    success_url='/empresa/sedes/actualizar/{id}'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Sede.objects.get(id=self.kwargs['pk'])
        context["consulta"] = DetalleModel.objects.filter(sede_id=self.kwargs['pk'])
        return context

class SedeDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Empresa.delete_sede'
    def get(self,request,**kwargs):
        ide = self.kwargs['pk']
        query = get_object_or_404(Sede,id=ide)
        query.delete()
        return redirect('empresa:sedeIndex')


class DependenciaCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url='/auth/login'
    permission_required='Empresa.add_dependencia'
    model = Dependencia
    fields = ['dependencia',]
    form = DependenciaForm
    template_name='Empresa/Dependencia/index.html'
    success_url="."
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['query']=Dependencia.objects.all()
        return context

class DependenciaUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='/auth/login'
    permission_required='Empresa.change_dependencia'
    model = Dependencia
    fields = ['dependencia',]
    form = DependenciaForm
    template_name='Empresa/Dependencia/update.html'
    success_url='/empresa/dependencias/actualizar/{id}'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['query']=Dependencia.objects.get(id=self.kwargs['pk'])
        return context

class DependenciaDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Empresa.delete_dependencia'
    def get(self,request,**kwargs):
        ide = self.kwargs['pk']
        query = get_object_or_404(Dependencia,id=ide)
        query.delete()
        return redirect('empresa:dependenciaIndex')

class SedeDependencia(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Empresa.add_sededependencia'
    def get(self,request,**kwargs):
        ide = self.kwargs['pk']
        context ={
        'sede':Sede.objects.get(id=ide),
        'query':Dependencia.objects.all(),
        }
        return render(request,'Empresa/SedeDependencia/detalles.html',context)

class add(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Empresa.view_sededependencia'
    def get(self,request,**kwargs):
        ide = self.kwargs['pk']
        queryset = Dependencia.objects.get(id=ide)
        d = detalle(self.request)
        d.add(queryset)
        aux = request.session["sede"]
        for row in aux.keys():
            id=aux[row]['sede_id']
        return redirect('empresa:sedeDep',str(id))
class remove(LoginRequiredMixin,PermissionRequiredMixin,View):
        login_url='/auth/login'
        permission_required='Empresa.view_sededependencia'
        def get(self,request,**kwargs):
            ide = self.kwargs['pk']
            queryset = Dependencia.objects.get(id=ide)
            d = detalle(self.request)
            d.remove(queryset)
            aux = request.session["sede"]
            for row in aux.keys():
                id=aux[row]['sede_id']
            return redirect('empresa:sedeDep',str(id))

class cls(LoginRequiredMixin,PermissionRequiredMixin,View):
        login_url='/auth/login'
        permission_required='Empresa.view_sededependencia'
        def get(self,request,**kwargs):
            d =detalle(self.request)
            d.clear()
            aux = request.session["sede"]
            for row in aux.keys():
                id=aux[row]['sede_id']
            return redirect('empresa:sedeDep',str(id))
class todos(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Empresa.view_sededependencia'
    def get(self,request,**kwargs):
        queryset = Dependencia.objects.all()
        d =detalle(self.request)
        for element in queryset:
            d.add(element)
        aux = request.session["sede"]
        for row in aux.keys():
            id=aux[row]['sede_id']
        return redirect('empresa:sedeDep',str(id))

class store(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Empresa.view_sededependencia'
    def get(self,request,**kwargs):
        aux = request.session["sede"]
        d = request.session["detalle"]
        det =detalle(self.request)
        s = sede(self.request)
        for row in aux.keys():
            id=aux[row]['sede_id']
        for row in d.keys():
            ide=d[row]['dependencia_id']
            DetalleModel.objects.create(sede_id=id,dependencia_id=ide)
        det.clear()
        s.clear()
        return redirect('empresa:sedeUpdate',str(id))

class delSedeDep(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Empresa.delete_sededependencia'
    def get(self,request,**kwargs):
        ide = self.kwargs['pk']
        s = self.kwargs['sede']
        DetalleModel.objects.get(sede=s,id=ide).delete()
        return redirect('empresa:sedeUpdate',str(s))
