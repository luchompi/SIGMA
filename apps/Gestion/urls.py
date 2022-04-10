from django.urls import path
from . import views as v

app_name="gestion"


urlpatterns=[
path('asignaciones/',v.AsignacionListView.as_view(),name="asignacionIndex"),
path('asignaciones/query?_<pk>',v.AsignacionDetails.as_view(),name="funcAsigDetail"),

]