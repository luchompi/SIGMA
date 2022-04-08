from django import forms

ESTADO=[
('pendiente','Por Asignar'),
('baja','En Proceso de Baja'),
('activo','ACTIVO')
('mantenimiento','En Mantenimiento')
]

INGRESOS =[
('compra','Compra Directa'),
('donacion','Donacion'),
('transferencia','Transferencia tecnologica'),
('traspaso','Traspaso de otra sede')
]

class marcaForm(forms.Form):
	marca = forms.CharField()
	
class modeloForm(forms.Form):
	modelo = forms.CharField()

class elementoForm(forms.Form):
	Serial=forms.CharField()
	conexionRed=forms.BooleanField()
	ip = forms.GenericIPAddressField()
	nombreRed=forms.CharField()
	mac=forms.CharField()
	valorAdquisicion=forms.DecimalField()
	proveedor=forms.Select(queryset=Proveedor.objects.all())
	modelo=forms.select(queryset=Modelo.objects.all())
	estado=forms.CharField(choices=ESTADO)
	tipoIngreso=forms.CharField(choices=INGRESOS)