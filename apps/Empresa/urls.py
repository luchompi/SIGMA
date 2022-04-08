from django.urls import path
from . import views as v
app_name="empresa"
urlpatterns=[
#sedes URLS
path('sedes/',v.SedeCreate.as_view(),name="sedeIndex"),
path('sedes/actualizar/<pk>',v.SedeUpdate.as_view(),name="sedeUpdate"),
path('sedes/delete/<pk>',v.SedeDelete.as_view(),name="sedeDel"),

#dependencias URLS
path('dependencias/',v.DependenciaCreate.as_view(),name="dependenciaIndex"),
path('dependencias/actualizar/<pk>',v.DependenciaUpdate.as_view(),name="dependenciaUpdate"),
path('dependencias/delelete/<pk>',v.DependenciaDelete.as_view(),name="dependenciaDel"),

#detalles de Sedes
path('sedes/add_dependencia/<pk>',v.SedeDependencia.as_view(),name="sedeDep"),
path('add/<pk>',v.add.as_view(),name="add"),
path('remove/<pk>',v.remove.as_view(),name="remove"),
path('cls/',v.cls.as_view(),name="cls"),
path('todo/',v.todos.as_view(),name="todos"),
path('store/',v.store.as_view(),name="store"),
path('sedes/delDep/<sede>/<pk>',v.delSedeDep.as_view(),name="borrar"),
]
