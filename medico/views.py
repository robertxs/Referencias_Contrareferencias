#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import *
from django.views.generic import *
from medico.forms import *
from medico.models import *
from medico.controllers import *


class PerfilMedico(TemplateView):
    template_name = 'medico/perfil_medico.html'


class VerConsultas(TemplateView):
    template_name = 'medico/ver_consultas.html'


class HistoriasClinicas(TemplateView):
    template_name = 'medico/historias_clinicas.html'


class BuscarPaciente(TemplateView):
    template_name = 'medico/buscar.html'


class BuscarMedico(TemplateView):
    template_name = 'medico/buscar.html'


class VerCitas(TemplateView):
    template_name = 'medico/ver_citas.html'

