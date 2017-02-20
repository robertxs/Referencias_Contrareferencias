#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import *
from django.views.generic import *
from administrador.forms import *
from paciente.forms import *
from paciente.models import *
from paciente.controllers import *
from administrador.models import *
import datetime
import calendar
import parsedatetime as pdt


class BuscarMedico(TemplateView):
    template_name = 'medico/buscar.html'

    def get_context_data(self, **kwargs):
        context = super(
            BuscarMedico, self).get_context_data(**kwargs)

        medicos = Medico.objects.all()

        context['result'] = medicos

        return context

class VerCitasPaciente(TemplateView):
    template_name = 'paciente/ver_citas_paciente.html'

    def get_context_data(self, **kwargs):
        context = super(
            VerCitasPaciente, self).get_context_data(**kwargs)
        user = user = User.objects.get(pk=self.kwargs['id'])
        citas = Medico_Citas.objects.filter(
            paciente__usuario__user=user)

        context['appointments'] = citas

        return context


class AgregarCitasPaciente(CreateView):
    template_name = 'paciente/agregar_cita_paciente.html'
    form_class = Paciente_CitasForm

    def get_context_data(self, **kwargs):
        context = super(
            AgregarCitasPaciente, self).get_context_data(**kwargs)

        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Paciente_CitasForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user_pk = request.user.pk
            medico = request.POST['medico']
            institucion = request.POST['institucion']
            fecha = request.POST['fecha']
            descripcion = request.POST['descripcion']
            value = agregar_citas_paciente(user_pk, medico, institucion, descripcion,
                                  fecha)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'ver_citas_paciente', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('paciente/agregar_cita_paciente.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            messages.error(request,"Por favor verifique que los campos estan en color rojo.")
            return render_to_response('paciente/agregar_cita_paciente.html',
                                      {'form': form,
                                       'title': 'Agregar'},
                                      context_instance=RequestContext(request))


class ModificarCitasPaciente(CreateView):
    template_name = 'medico/agregar_cita.html'
    form_class = Paciente_CitasForm

    def get_context_data(self, **kwargs):
        context = super(
            ModificarCitas, self).get_context_data(**kwargs)

        context['title'] = 'Modificar'
        cita = Medico_Citas.objects.get(pk=self.kwargs['id'])
        data = {'paciente': cita.paciente,
                'descripcion': cita.descripcion,
                'fecha': cita.fecha
                }
        form = Paciente_CitasForm(initial=data)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Paciente_CitasForm(request.POST)
        if form.is_valid():
            cita_id = kwargs['id']
            paciente = request.POST['paciente']
            descripcion = request.POST['descripcion']
            fecha = request.POST['fecha']
            value = modificar_citas(cita_id, paciente, descripcion,
                                    fecha)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'ver_citas', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('paciente/agregar_cita.html',
                                          {'form': form,
                                           'title': 'Modificar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('paciente/agregar_cita.html',
                                      {'form': form,
                                       'title': 'Modificar'},
                                      context_instance=RequestContext(request))
