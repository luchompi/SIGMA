from django import forms
from apps.Empresa.models import SedeDependencia
from .models import Funcionario
class funcionarioForm(forms.ModelForm):
   
    class Meta:
        model = Funcionario
        fields = ('identificacion','nombres','apellidos','direccion','telefono','correo','sede',)
    
class proveedorForm(forms.Form):
    NIT=forms.CharField()
    razonSocial=forms.CharField()
    direccion=forms.CharField()
    dir_venta=forms.CharField()
    telefono1=forms.CharField()
    telefono2=forms.CharField()
    correo=forms.EmailField()
    vendedor=forms.CharField()
    tel_vendedor=forms.CharField()
