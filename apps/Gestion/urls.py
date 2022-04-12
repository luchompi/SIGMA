from django.urls import path
from . import views as v

app_name="gestion"


urlpatterns=[
path('asignaciones/',v.AsignacionListView.as_view(),name="asignacionIndex"),
path('asignaciones/query?_<pk>',v.AsignacionDetails.as_view(),name="funcAsigDetail"),
path('asignaciones/fc=&<pk>',v.Func2Session.as_view(),name="func2Session"),
path('asignaciones/add/fc=&<iden>/<pk>',v.add2Session.as_view(),name="add2Session"),
path('asignaciones/del/fc=&<iden>/<pk>',v.del2Session.as_view(),name="del2Session"),
path('asignaciones/cls/fc=&<iden>/',v.cancel.as_view(),name="cls2Session"),
path('asignaciones/complete_fc=&<iden>/',v.successAsignacion.as_view(),name="successAsignacion"),
path('asignaciones/view?_<pk>',v.AsigQuery.as_view(),name="AsigQuery"),
path('asignaciones/report_single=&<pk>.<iden>',v.PDF.as_view(),name="PDFsingle"),
]