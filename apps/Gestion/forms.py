from django import forms
from apps.Personas.models import Funcionario
class traspasos(forms.Form):
    funcionario = forms.ModelChoiceField(queryset=Funcionario.objects.all())
