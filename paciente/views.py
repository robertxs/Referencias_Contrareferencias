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

class Perfil(CreateView):
    template_name = 'medico/perfil_medico.html'
    form_class = UsuarioForm
    print("saliooooo")
    def get_context_data(self, **kwargs):

        context = super(
            Perfil, self).get_context_data(**kwargs)

        user = self.request.user
        usuario = Usuario.objects.get(user=user)
        print("en perfil" + str(usuario))
        try:
            paciente = Paciente.objects.get(usuario=usuario)
        except:
            paciente = Paciente(cedula=usuario.ci, first_name=user.first_name,
                            last_name=user.last_name, fecha_nacimiento=None,
                            lugar_nacimiento='', ocupacion='',
                            sexo='', estado_civil='', telefono='',
                            direccion='', usuario=usuario)
            paciente.save()
        data = {'first_name': paciente.usuario.user.first_name,
                'last_name': paciente.usuario.user.last_name,
                'email': paciente.usuario.user.email}
        form = UsuarioForm(initial=data)
        context['paciente'] = paciente
        context['form'] = form
        context['usuario'] = usuario
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = UsuarioForm(request.POST, request.FILES)
        form.fields['username'].required = False
        form.fields['passw'].required = False
        form.fields['ci'].required = False
        form.fields['rol'].required = False
        print(form.is_valid())
        if form.is_valid():
            nombre = request.POST['first_name']
            apellido = request.POST['last_name']
            sexo = request.POST['sex']
            fecha = request.POST['birth_date']
            estado_civil = request.POST['marital_status']
            lugar = request.POST['lugar']
            telefono = request.POST['phone']
            email = request.POST['email']
            direccion = request.POST['address']
            ocupacion = request.POST['ocupacion']
            if (request.FILES!={}):
                foto = request.FILES['image']
                print("en tryyyy")
            else:
                foto = False
                print("exceptttttt")
            
            print("antes del value")
            print(nombre)
            print(apellido)
            print(lugar)
            value = editar_paciente(request.user, nombre, apellido, sexo, ocupacion,
                                  fecha, lugar, estado_civil, telefono, direccion, email, foto)
            print("despues de valueeee" + str(value))
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_paciente', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/perfil_medico.html',
                                          {'form': form},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/perfil_medico.html',
                                      {'form': form},
                                      context_instance=RequestContext(request))


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
    template_name = 'medico/agregar_cita.html'
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
        form = Paciente_CitasForm(request.POST,paciente=request.user.pk)
        if form.is_valid():
            user_pk = request.user.pk
            medico = request.POST['medico']
            institucion = request.POST['institucion']
            fecha = request.POST['fecha']
            descripcion = request.POST['descripcion']
            hora = request.POST['hora']
            especialidad = request.POST['especialidad']
            value = agregar_citas_paciente(user_pk, medico, institucion, descripcion,
                                  fecha,hora,especialidad, es_referido= False)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'ver_citas_pac', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_cita.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            messages.error(request,"Por favor verifique los campos siguientes:")
            return render_to_response('medico/agregar_cita.html',
                                      {'form': form,
                                       'title': 'Agregar'},
                                      context_instance=RequestContext(request))


class ModificarCitasPaciente(CreateView):
    template_name = 'medico/agregar_cita.html'
    form_class = Paciente_CitasForm

    def get_context_data(self, **kwargs):
        context = super(
            ModificarCitasPaciente, self).get_context_data(**kwargs)

        context['title'] = 'Modificar'
        cita = Medico_Citas.objects.get(pk=self.kwargs['id'])
        data = {'descripcion': cita.descripcion,
                'fecha': cita.fecha,
                'institucion': cita.institucion,
                'especialidad': cita.especialidad,
                'medico': cita.medico,
                'hora': cita.hora,
                }
        form = Paciente_CitasForm(initial=data)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Paciente_CitasForm(request.POST,paciente=request.user.pk)
        print(form.is_valid())
        if form.is_valid():
            cita_id = kwargs['id']
            medico = request.POST['medico']
            descripcion = request.POST['descripcion']
            fecha = request.POST['fecha']
            hora = request.POST['hora']
            especialidad = request.POST['especialidad']
            institucion = request.POST['institucion']
            value = modificar_citas_paciente(cita_id, medico, institucion, descripcion,
                                  fecha,hora,especialidad, es_referido= False)
            print(value)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'ver_citas_pac', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_cita.html',
                                          {'form': form,
                                           'title': 'Modificar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_cita.html',
                                      {'form': form,
                                       'title': 'Modificar'},
                                      context_instance=RequestContext(request))


class Informe(TemplateView):
    template_name = 'paciente/informe_med.html'

    def get_context_data(self, **kwargs):
        context = super(
            Informe, self).get_context_data(**kwargs)
        user = user = User.objects.get(pk=self.kwargs['id'])
        citas = Medico_Citas.objects.filter(
            paciente__usuario__user=user)

        context['appointments'] = citas

        return context
