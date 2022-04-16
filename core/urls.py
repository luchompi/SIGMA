"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404,handler500
from apps.Home.views import error,Error500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.Home.urls",namespace="home")),
    path('empresa/', include("apps.Empresa.urls",namespace="empresa")),
    path('personas/', include("apps.Personas.urls",namespace="personas")),
    path('inventario/', include("apps.Inventario.urls",namespace="inventario")),
    path('gestion/', include("apps.Gestion.urls",namespace="gestion")),
    path('manteniminetos/', include("apps.Mantenimiento.urls",namespace="mantenimiento")),
    path('auth/', include("django.contrib.auth.urls")),
]
handler404 = error.as_view()
handler500 = Error500.as_error_view()
