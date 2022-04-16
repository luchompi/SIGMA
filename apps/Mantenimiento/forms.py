from django import forms

class mantenimientoForm(forms.Form):
    descripcion = forms.CharField(widget=forms.Textarea,label='Descripción de la solicitud de Mantenimiento')
class CierreCasoForm(forms.Form):
    observaciones = forms.CharField(widget=forms.Textarea,label='Observaciones del mantenimiento')
    irreparable = forms.BooleanField(label='¿El elemento es irreparable?',required=False)

    