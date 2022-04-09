from django.shortcuts import render,redirect
from .models import Marca,Modelo,Elemento
from .forms import marcaForm,modeloForm,elementoForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,View,DetailView
from datetime import datetime as dt
from .utils import render_to_pdf
from django.http import HttpResponse


#Operaciones con Marcas
class MarcaCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url='/auth/login'
    permission_required='Inventario.add_marca'
    model = Marca
    form = marcaForm
    fields =['marca']
    success_url='.'
    template_name = "Inventario/Marcas/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Marca.objects.all()
        return context

class MarcaUpdateView(UpdateView):
    login_url='/auth/login'
    permission_required='Inventario.add_marca'
    model = Marca
    form = marcaForm
    fields =['marca']
    success_url='/inventario/marcas/detalles/{id}'
    template_name = "Inventario/Marcas/update.html"

class ModeloCreateView(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Inventario.add_modelo'
    def get(self,request,**kwargs):
        ide =self.kwargs['pk']
        form = modeloForm
        context = {'object':Marca.objects.get(id=ide),'form':form,'data':Modelo.objects.filter(marca_id=ide)}
        return render(request,"Inventario/Marcas/details.html",context)
    def post(self,request,**kwargs):
        ide = self.kwargs['pk']
        form = modeloForm(request.POST)
        if form.is_valid():
            mod = form.cleaned_data['modelo']
            Modelo.objects.create(marca_id=ide,modelo=mod)
            return redirect('inventario:marcaModel',str(ide))

class ModeloDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Inventario.delete_modelo'
    def get(self,request,**kwargs):
        ide = self.kwargs['pk']
        modelo = self.kwargs['id']
        Modelo.objects.get(id=modelo,marca_id=ide).delete()
        return redirect('inventario:marcaModel',str(ide))

class MarcaDelete(View):
    def get(self,request,**kwargs):
        ide = self.kwargs['pk']
        Marca.objects.get(id=ide).delete()
        return redirect('inventario:marcaIndex')

#Operaciones con Elementos
class ElementoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    login_url='/auth/login'
    permission_required = 'Inventario.view_elemento'
    model = Elemento
    template_name = "Inventario/Elementos/index.html"

class ElementoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url='/auth/login'
    permission_required='Inventario.add_elemento'
    model = Elemento
    form = elementoForm
    fields = ['Serial','conexionRed','ip','nombreRed','mac','valorAdquisicion','proveedor','modelo','estado','tipoIngreso']
    template_name = "Inventario/Elementos/create.html"
    def form_valid(self,form):
        var = form.cleaned_data['ip']
        if var:
            q = form.cleaned_data['mac']
            form.save()
            query = Elemento.objects.get(mac=q)
            query.conexionRed=True
            query.save()
            return redirect('inventario:elementoDetail',str(query.placa))
        else:
            q = form.cleaned_data['mac']
            form.save()
            query = Elemento.objects.get(mac=q)
            form.save()
            return redirect('inventario:elementoDetail',str(query.placa))

class ElementoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='/auth/login'
    permission_required  = 'Inventario.change_elemento'
    model = Elemento
    template_name="Inventario/Elementos/details.html"
    form = elementoForm
    fields = ['Serial','conexionRed','ip','nombreRed','mac','valorAdquisicion','proveedor','modelo','estado','tipoIngreso']
    template_name = "Inventario/Elementos/details.html"
    def form_valid(self,form):
        var = form.cleaned_data['ip']
        if var:
            form.save()
            query = Elemento.objects.get(ip=var)
            query.conexionRed=True
            query.save()
            return redirect('inventario:elementoDetail',str(self.kwargs['pk']))
        else:
            form.save()
            return redirect('inventario:elementoDetail',str(self.kwargs['pk']))

class ElementoDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Inventario.delete_elemento'
    def get(self,request,**kwargs):
        ide = self.kwargs['pk']
        Elemento.objects.get(placa=ide).delete()
        return redirect('inventario:elementoIndex')

class PDFGeneral(LoginRequiredMixin,PermissionRequiredMixin,View):
    login_url='/auth/login'
    permission_required='Inventario.view_elemento'
    def get(self,request,*args,**kwargs):
        context = {'query': Elemento.objects.all(),'timestamps':dt.now(),'usuario':request.user,}
        pdf = render_to_pdf('Inventario/Elementos/PDFGeneral.html', context)
        return HttpResponse(pdf, content_type='application/pdf')