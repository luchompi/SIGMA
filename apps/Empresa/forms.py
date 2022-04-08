from django import forms
from .models import Dependencia,Sede

class DependenciaForm(forms.ModelForm):
    class Meta:
        model = Dependencia
        fields = ['dependencia',]

class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ['sede',]

class addDependenciaForm(forms.Form):
    dependencia = forms.ModelChoiceField(queryset=Dependencia.objects.all())
