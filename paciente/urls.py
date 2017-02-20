"""paciente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from paciente.views import *

urlpatterns = [
    url(
        r'^ver-citas-paciente/(?P<id>\w+)$',
        VerCitasPaciente.as_view(),
        name='ver_citas_paciente'
    ),
    url(
        r'^agregar-cita-paciente/(?P<id>\w+)$',
        AgregarCitasPaciente.as_view(),
        name='agregar_cita_paciente'
    ),
    url(
        r'^modificar-cita-paciente/(?P<id>\w+)$',
        ModificarCitasPaciente.as_view(),
        name='modificar_cita_paciente'
    ),
    url(
        r'^eliminar-cita-paciente/(?P<id>\w+)$',
        'medico.controllers.eliminar_citas',
        name='eliminar_cita_paciente'
    ),
    url(
        r'^buscar-medico$',
        BuscarMedico.as_view(),
        name='buscar_medico_paciente'
    ),
]
