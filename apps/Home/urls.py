from django.urls import path
from . import views as v
app_name="home"

urlpatterns=[
path('',v.Home.as_view(),name="home"),
]