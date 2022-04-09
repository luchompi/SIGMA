from django.urls import path
from . import views as v

app_name="inventario"

urlpatterns =[
path('marcas/',v.MarcaCreateView.as_view(),name="marcaIndex"),
path('marcas/detalles/<pk>',v.MarcaUpdateView.as_view(),name="marcaUpdate"),
path('marcas/borrar/<pk>',v.MarcaDelete.as_view(),name="marcaDelete"),
path('marcas/add_model/<pk>',v.ModeloCreateView.as_view(),name="marcaModel"),
path('marcas/del_model/<pk>/<id>',v.ModeloDelete.as_view(),name="delMarcaModel"),

path('elementos/',v.ElementoListView.as_view(),name="elementoIndex"),
path('elementos/nuevo',v.ElementoCreateView.as_view(),name="elementoCreate"),
path('elementos/detalles/<pk>',v.ElementoUpdateView.as_view(),name="elementoDetail"),
path('elementos/eliminar/<pk>',v.ElementoDelete.as_view(),name="elementoDelete"),
]