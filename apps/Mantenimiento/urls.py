from django.urls import path as p
from . import views as v

app_name="mantenimiento"

urlpatterns = [
p('',v.ElementoList.as_view(),name="elementoList"),
p('details?_<pk>',v.MantenimientoDetail.as_view(),name="mantenimientoDetails"),
p('new/element=<pk>/',v.Mantenimiento.as_view(),name="mantenimientoCreate"),
p('record/PID=<pk>/',v.DetalleCaso.as_view(),name="mantenimientoRecord"),
p('close/PID=<pk>/',v.CerrarCaso.as_view(),name="cerrarCaso"),

]