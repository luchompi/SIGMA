from django.urls import path
from . import views as v

app_name="personas"


urlpatterns=[
path('funcionarios/',v.FuncionarioListView.as_view(),name="funcIndex"),
path('funcionarios/crear/',v.FuncionarioCreateView.as_view(),name="funcCreate"),
path('funcionarios/detalles/<pk>',v.FuncionarioUpdateView.as_view(),name="funcUpdate"),
path('funcionarios/borrar/<pk>',v.FuncionarioDeleteView.as_view(),name="funcDelete"),
path('funrionarios/report/<pk>',v.PDF.as_view(),name="funcPDF"),

path('proveedores/',v.ProveedorListView.as_view(),name="proovIndex"),
path('proveedores/crear/',v.ProveedorCreateView.as_view(),name="proovCreate"),
path('proveedores/detalles/<pk>',v.ProveedorUpdateView.as_view(),name="proovUpdate"),
path('proveedores/borrar/<pk>',v.ProveedorDeleteView.as_view(),name="proovDelete"),
]