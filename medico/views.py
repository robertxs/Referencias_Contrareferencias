#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth import *
from django.contrib import messages
from django.views.generic import *
from administrador.forms import *
from medico.forms import *
from paciente.forms import *
from medico.models import *
from medico.controllers import *
from administrador.models import *
import datetime
import calendar
import parsedatetime as pdt
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.lib.enums  import *
from io import BytesIO


class PerfilMedico(CreateView):
    template_name = 'medico/perfil_medico.html'
    form_class = PerfilForm

    def get_context_data(self, **kwargs):
        context = super(
            PerfilMedico, self).get_context_data(**kwargs)
        user = self.request.user
        usuario = Usuario.objects.get(user=user)
        try:
            medico = Medico.objects.get(usuario=usuario)
        except:
            medico = Medico(cedula=usuario.ci, first_name=user.first_name,
                            last_name=user.last_name, fecha_nacimiento=None,
                            sexo='', estado_civil='', telefono='',
                            direccion='', usuario=usuario, foto = None)
            medico.save()
        data = {'first_name': medico.usuario.user.first_name,
                'last_name': medico.usuario.user.last_name,
                'email': medico.usuario.user.email}
        form = UsuarioForm(initial=data)
        estudios = Medico_Estudios.objects.filter(medico=medico)
        logros = Medico_Logros.objects.filter(medico=medico)
        publicaciones = Medico_Publicaciones.objects.filter(medico=medico)
        experiencias = Medico_Experiencias.objects.filter(medico=medico)
        habilidades = Medico_Habilidades.objects.filter(medico=medico)
        eventos = Medico_Eventos.objects.filter(medico=medico)
        context['usuario'] = usuario
        context['medico'] = medico
        context['studies'] = estudios
        context['awards'] = logros
        context['publications'] = publicaciones
        context['experiences'] = experiencias
        context['abilities'] = habilidades
        context['events'] = eventos
        context['form'] = form
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
        #form.fields['foto'].required = False
        print("for valido")
        print(form.is_valid())
        if form.is_valid():
            nombre = request.POST['first_name']
            apellido = request.POST['last_name']
            email = request.POST['email']
            sexo = request.POST['sex']
            fecha = request.POST['birth_date']
            estado_civil = request.POST['marital_status']
            telefono = request.POST['phone']
            direccion = request.POST['address']
            print(request.FILES=={})
            if (request.FILES!={}):
                foto = request.FILES['image']
                print("en tryyyy")
            else:
                foto = False
                print("exceptttttt")
            print("ESTA ES LA FOTO")
            #print(foto)
            value = editar_medico(request.user, nombre, apellido, email, sexo,
                                  fecha, estado_civil, telefono, direccion, foto)

            print(value)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/perfil_medico.html',
                                          {'form': form},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/perfil_medico.html',
                                      {'form': form},
                                      context_instance=RequestContext(request))


class AgregarEstudios(CreateView):
    template_name = 'medico/agregar_estudios.html'
    form_class = Medico_EstudiosForm

    def get_context_data(self, **kwargs):
        context = super(
            AgregarEstudios, self).get_context_data(**kwargs)

        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_EstudiosForm(request.POST)
        if form.is_valid():
            user_pk = request.user.pk
            titulo = request.POST['titulo']
            fecha_graduacion = request.POST['fecha_graduacion']
            descripcion = request.POST['descripcion']
            institucion = request.POST['institucion']
            value = agregar_estudios(user_pk, titulo, fecha_graduacion,
                                     descripcion, institucion)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_estudios.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_estudios.html',
                                      {'form': form,
                                       'title': 'Agregar'},
                                      context_instance=RequestContext(request))


class ModificarEstudios(CreateView):
    template_name = 'medico/agregar_estudios.html'
    form_class = Medico_EstudiosForm

    def get_context_data(self, **kwargs):
        context = super(
            ModificarEstudios, self).get_context_data(**kwargs)

        context['title'] = 'Modificar'
        print self.request.GET
        estudio = Medico_Estudios.objects.get(pk=self.kwargs['id'])
        data = {'titulo': estudio.titulo,
                'fecha_graduacion': estudio.fecha_graduacion,
                'descripcion': estudio.descripcion,
                'institucion': estudio.institucion}
        form = Medico_EstudiosForm(initial=data)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_EstudiosForm(request.POST)
        if form.is_valid():
            estudio_id = kwargs['id']
            titulo = request.POST['titulo']
            fecha_graduacion = request.POST['fecha_graduacion']
            descripcion = request.POST['descripcion']
            institucion = request.POST['institucion']
            value = modificar_estudios(estudio_id, titulo,
                                       fecha_graduacion,
                                       descripcion, institucion)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_estudios.html',
                                          {'form': form,
                                           'title': 'Modificar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_estudios.html',
                                      {'form': form,
                                       'title': 'Modificar'},
                                      context_instance=RequestContext(request))


class AgregarReconocimientos(CreateView):
    template_name = 'medico/agregar_reconocimientos.html'
    form_class = Medico_LogrosForm

    def get_context_data(self, **kwargs):
        context = super(
            AgregarReconocimientos, self).get_context_data(**kwargs)

        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_LogrosForm(request.POST)
        if form.is_valid():
            user_pk = request.user.pk
            titulo = request.POST['titulo']
            fecha = request.POST['fecha']
            descripcion = request.POST['descripcion']
            value = agregar_reconocimientos(user_pk, titulo, fecha,
                                            descripcion)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_reconocimientos.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_reconocimientos.html',
                                      {'form': form,
                                       'title': 'Agregar'},
                                      context_instance=RequestContext(request))


class ModificarReconocimientos(CreateView):
    template_name = 'medico/agregar_reconocimientos.html'
    form_class = Medico_LogrosForm

    def get_context_data(self, **kwargs):
        context = super(
            ModificarReconocimientos, self).get_context_data(**kwargs)

        context['title'] = 'Modificar'
        logro = Medico_Logros.objects.get(pk=self.kwargs['id'])
        data = {'titulo': logro.titulo,
                'fecha': logro.fecha,
                'descripcion': logro.descripcion}
        form = Medico_LogrosForm(initial=data)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_LogrosForm(request.POST)
        if form.is_valid():
            logro_id = kwargs['id']
            titulo = request.POST['titulo']
            fecha = request.POST['fecha']
            descripcion = request.POST['descripcion']
            value = modificar_logros(logro_id, titulo, fecha,
                                     descripcion)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_reconocimientos.html',
                                          {'form': form,
                                           'title': 'Modificar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_reconocimientos.html',
                                      {'form': form,
                                       'title': 'Modificar'},
                                      context_instance=RequestContext(request))


class AgregarPublicaciones(CreateView):
    template_name = 'medico/agregar_publicaciones.html'
    form_class = Medico_PublicacionesForm

    def get_context_data(self, **kwargs):
        context = super(
            AgregarPublicaciones, self).get_context_data(**kwargs)

        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_PublicacionesForm(request.POST)
        if form.is_valid():
            user_pk = request.user.pk
            titulo = request.POST['titulo']
            autores = request.POST['autores']
            descripcion = request.POST['descripcion']
            revista = request.POST['revista']
            numero = request.POST['numero']
            volumen = request.POST['volumen']
            fecha = request.POST['fecha']
            value = agregar_publicaciones(user_pk, titulo, autores,
                                          descripcion, revista,
                                          numero, volumen, fecha)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_publicaciones.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_publicaciones.html',
                                      {'form': form,
                                       'title': 'Agregar'},
                                      context_instance=RequestContext(request))


class ModificarPublicaciones(CreateView):
    template_name = 'medico/agregar_publicaciones.html'
    form_class = Medico_PublicacionesForm

    def get_context_data(self, **kwargs):
        context = super(
            ModificarPublicaciones, self).get_context_data(**kwargs)

        context['title'] = 'Modificar'
        publicacion = Medico_Publicaciones.objects.get(pk=self.kwargs['id'])
        data = {'titulo': publicacion.titulo,
                'autores': publicacion.autores,
                'descripcion': publicacion.descripcion,
                'revista': publicacion.revista,
                'numero': publicacion.numero,
                'volumen': publicacion.volumen,
                'fecha': publicacion.fecha,
                }
        form = Medico_PublicacionesForm(initial=data)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_PublicacionesForm(request.POST)
        if form.is_valid():
            publicacion_id = kwargs['id']
            titulo = request.POST['titulo']
            autores = request.POST['autores']
            descripcion = request.POST['descripcion']
            revista = request.POST['revista']
            numero = request.POST['numero']
            volumen = request.POST['volumen']
            fecha = request.POST['fecha']
            value = modificar_publicaciones(publicacion_id, titulo, autores,
                                            descripcion, revista,
                                            numero, volumen, fecha)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_publicaciones.html',
                                          {'form': form,
                                           'title': 'Modificar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_publicaciones.html',
                                      {'form': form,
                                       'title': 'Modificar'},
                                      context_instance=RequestContext(request))


class AgregarExperiencias(CreateView):
    template_name = 'medico/agregar_experiencias.html'
    form_class = Medico_ExperienciasForm

    def get_context_data(self, **kwargs):
        context = super(
            AgregarExperiencias, self).get_context_data(**kwargs)

        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_ExperienciasForm(request.POST)
        if form.is_valid():
            user_pk = request.user.pk
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            fecha_inicio = request.POST['fecha_inicio']
            fecha_fin = request.POST['fecha_fin']
            institucion = request.POST['institucion']
            value = agregar_experiencias(user_pk, titulo, descripcion,
                                         fecha_inicio, fecha_fin, institucion)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_experiencias.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_experiencias.html',
                                      {'form': form,
                                       'title': 'Agregar'},
                                      context_instance=RequestContext(request))


class ModificarExperiencias(CreateView):
    template_name = 'medico/agregar_experiencias.html'
    form_class = Medico_ExperienciasForm

    def get_context_data(self, **kwargs):
        context = super(
            ModificarExperiencias, self).get_context_data(**kwargs)

        context['title'] = 'Modificar'
        experiencia = Medico_Experiencias.objects.get(pk=self.kwargs['id'])
        data = {'titulo': experiencia.titulo,
                'descripcion': experiencia.descripcion,
                'fecha_inicio': experiencia.fecha_inicio,
                'fecha_fin': experiencia.fecha_fin,
                'institucion': experiencia.institucion,
                }
        form = Medico_ExperienciasForm(initial=data)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_ExperienciasForm(request.POST)
        if form.is_valid():
            experiencia_id = kwargs['id']
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            fecha_inicio = request.POST['fecha_inicio']
            fecha_fin = request.POST['fecha_fin']
            institucion = request.POST['institucion']
            value = modificar_experiencias(experiencia_id, titulo, descripcion,
                                           fecha_inicio, fecha_fin,
                                           institucion)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_experiencias.html',
                                          {'form': form,
                                           'title': 'Modificar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_experiencias.html',
                                      {'form': form,
                                       'title': 'Modificar'},
                                      context_instance=RequestContext(request))


class AgregarHabilidades(CreateView):
    template_name = 'medico/agregar_habilidades.html'
    form_class = Medico_HabilidadesForm

    def get_context_data(self, **kwargs):
        context = super(
            AgregarHabilidades, self).get_context_data(**kwargs)

        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_HabilidadesForm(request.POST)
        if form.is_valid():
            user_pk = request.user.pk
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            value = agregar_habilidades(user_pk, titulo, descripcion)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_habilidades.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_habilidades.html',
                                      {'form': form,
                                       'title': 'Agregar'},
                                      context_instance=RequestContext(request))


class ModificarHabilidades(CreateView):
    template_name = 'medico/agregar_habilidades.html'
    form_class = Medico_HabilidadesForm

    def get_context_data(self, **kwargs):
        context = super(
            ModificarHabilidades, self).get_context_data(**kwargs)

        context['title'] = 'Modificar'
        habilidad = Medico_Habilidades.objects.get(pk=self.kwargs['id'])
        data = {'titulo': habilidad.titulo,
                'descripcion': habilidad.descripcion,
                }
        form = Medico_HabilidadesForm(initial=data)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_HabilidadesForm(request.POST)
        if form.is_valid():
            habilidad_id = kwargs['id']
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            value = modificar_habilidades(habilidad_id, titulo, descripcion)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_habilidades.html',
                                          {'form': form,
                                           'title': 'Modificar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_habilidades.html',
                                      {'form': form,
                                       'title': 'Modificar'},
                                      context_instance=RequestContext(request))


class AgregarEventos(CreateView):
    template_name = 'medico/agregar_eventos.html'
    form_class = Medico_EventosForm

    def get_context_data(self, **kwargs):
        context = super(
            AgregarEventos, self).get_context_data(**kwargs)

        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_EventosForm(request.POST)
        if form.is_valid():
            user_pk = request.user.pk
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            institucion = request.POST['institucion']
            fecha = request.POST['date']
            value = agregar_eventos(user_pk, titulo, descripcion,
                                    institucion, fecha)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_eventos.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_eventos.html',
                                      {'form': form,
                                       'title': 'Agregar'},
                                      context_instance=RequestContext(request))


class ModificarEventos(CreateView):
    template_name = 'medico/agregar_eventos.html'
    form_class = Medico_EventosForm

    def get_context_data(self, **kwargs):
        context = super(
            ModificarEventos, self).get_context_data(**kwargs)

        context['title'] = 'Modificar'
        evento = Medico_Eventos.objects.get(pk=self.kwargs['id'])
        data = {'titulo': evento.titulo,
                'descripcion': evento.descripcion,
                'institucion': evento.institucion,
                'date': evento.date
                }
        form = Medico_EventosForm(initial=data)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_EventosForm(request.POST)
        if form.is_valid():
            evento_id = kwargs['id']
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            institucion = request.POST['institucion']
            date = request.POST['date']
            value = modificar_eventos(evento_id, titulo, descripcion,
                                      institucion, date)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_eventos.html',
                                          {'form': form,
                                           'title': 'Modificar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_eventos.html',
                                      {'form': form,
                                       'title': 'Modificar'},
                                      context_instance=RequestContext(request))


class VerConsultas(TemplateView):
    template_name = 'medico/ver_consultas.html'

    def get_context_data(self, **kwargs):
        context = super(
            VerConsultas, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['id'])
        consultas = Medico_Especialidad.objects.filter(
            medico__usuario__user=user).order_by('especialidad')
        # b = []
        # for c in consultas :
        #     horario= c.horario
        #     horario2=horario.split(', ')
        #     i = 0
        #     a = ''
        #     for x in horario2 :
        #         ulti = i == (len(horario2)-1)
        #         elem=volverElemlista(x,ulti)
        #         a = a + elem + ', '
        #         i = i+1
        #     b.append(a)

        context['consultations'] = consultas
        # context['horario'] = b

        return context


class ModificarConsultas(CreateView):
    template_name = 'medico/agregar_consulta.html'
    form_class = Medico_HorariosFormEditar

    def get_context_data(self, **kwargs):
        context = super(
            ModificarConsultas, self).get_context_data(**kwargs)

        context['title'] = 'Modificar'
        consulta = Medico_Especialidad.objects.get(pk=self.kwargs['id'])
        data = {'especialidad': consulta.especialidad,
                'institucion': consulta.institucion,
                'horario' : consulta.horario,
                'medico' : consulta.medico
                }
        form = Medico_HorariosFormEditar(initial=data)
        context['form'] = form
        context['horario'] = consulta
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_HorariosFormEditar(request.POST)
        if form.is_valid():
            consulta_id = kwargs['id']
            medico = kwargs['user']
            horarios = request.POST['result_horario']
            print(horarios=='')
            if( horarios == ''):
                consulta = Medico_Especialidad.objects.get(pk=consulta_id)
                messages.error(request,"Por favor seleccione horarios de consulta.")
                return render_to_response('medico/agregar_consulta.html',
                                          {'form': form,
                                           'title': 'Modificar',
                                           'horario': consulta},
                                          context_instance=RequestContext(request))

            hora = horarios.split(",")
            horario=[]

            for x in hora :
                if not(x==''):
                    y= x.split(' ')
                    horario.append(y)

            value = modificar_consultas(consulta_id, medico, horario)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'ver_consultas', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_consulta.html',
                                          {'form': form,
                                           'title': 'Modificar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/agregar_consulta.html',
                                      {'form': form,
                                       'title': 'Modificar'},
                                      context_instance=RequestContext(request))


class AgregarConsulta(CreateView):
    template_name = 'medico/agregar_consulta.html'
    form_class = Medico_HorariosForm

    def get_context_data(self, **kwargs):
        context = super(
            AgregarConsulta, self).get_context_data(**kwargs)

        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_HorariosForm(request.POST,medico=request.user.pk)

        if form.is_valid():
            user_pk = request.user.pk
            especialidad = request.POST['especialidad']
            institucion = request.POST['institucion']
            horarios = request.POST['result_horario']
            print(horarios=='')
            if( horarios == ''):
                messages.error(request,"Por favor seleccione horarios de consulta.")
                return render_to_response('medico/agregar_consulta.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(request))

            hora = horarios.split(",")
            horario=[]

            for x in hora :
                if not(x==''):
                    y= x.split(' ')
                    horario.append(y)

            value = agregar_consultas(user_pk, especialidad, institucion,horario)

            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'ver_consultas', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/agregar_consulta.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            messages.error(request,"Por favor verifique los campos siguientes:")
            return render_to_response('medico/agregar_consulta.html',
                                      {'form': form,
                                       'title': 'Agregar'},
                                      context_instance=RequestContext(request))


class BuscarPaciente(TemplateView):
    template_name = 'medico/buscar.html'

    def get_context_data(self, **kwargs):
        context = super(
            BuscarPaciente, self).get_context_data(**kwargs)

        pacientes = Paciente.objects.all()
        variable = True

        context['result'] = pacientes
        context['paciente'] = variable

        return context


class BuscarMedico(TemplateView):
    template_name = 'medico/buscar.html'

    def get_context_data(self, **kwargs):
        context = super(
            BuscarMedico, self).get_context_data(**kwargs)

        medicos = Medico.objects.all()
        variable = False

        context['paciente'] = variable
        context['result'] = medicos

        return context


class VerCitas(TemplateView):
    template_name = 'medico/ver_citas.html'

    def get_context_data(self, **kwargs):
        context = super(
            VerCitas, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['id'])
        print(user.id)
        grupo = Group.objects.get(user=user.id)
        if (grupo.name == 'paciente') :
            citas = Medico_Citas.objects.filter(
                paciente__usuario__user=user).order_by('fecha')
        else :
            citas = Medico_Citas.objects.filter(
                medico__usuario__user=user).order_by('fecha')

        context['appointments'] = citas

        return context


class AgregarCitas(CreateView):
    template_name = 'medico/agregar_cita.html'
    form_class = Medico_CitasForm

    def get_context_data(self, **kwargs):
        context = super(
            AgregarCitas, self).get_context_data(**kwargs)

        context['title'] = 'Agregar'

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_CitasForm(request.POST,medico=request.user.pk)
        if form.is_valid():
            user_pk = request.user.pk
            paciente = request.POST['paciente']
            institucion = request.POST['institucion']
            fecha = request.POST['fecha']
            hora = request.POST['hora']
            descripcion = request.POST['descripcion']
            especialidad = request.POST['especialidad']
            value = agregar_citas(user_pk, paciente, institucion, descripcion,
                                  fecha,hora,especialidad, es_referido= False)

            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'ver_citas', kwargs={'id': request.user.pk}))
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


class ModificarCitas(CreateView):
    template_name = 'medico/agregar_cita.html'
    form_class = Medico_CitasForm

    def get_context_data(self, **kwargs):
        context = super(
            ModificarCitas, self).get_context_data(**kwargs)

        context['title'] = 'Modificar'
        cita = Medico_Citas.objects.get(pk=self.kwargs['id'])
        data = {'paciente': cita.paciente,
                'descripcion': cita.descripcion,
                'fecha': cita.fecha,
                'institucion': cita.institucion,
                'especialidad':cita.especialidad,
                'hora':cita.hora,
                }
        form = Medico_CitasForm(initial=data)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_CitasForm(request.POST,medico=request.user.pk)
        if form.is_valid():
            cita_id = kwargs['id']
            paciente = request.POST['paciente']
            descripcion = request.POST['descripcion']
            fecha = request.POST['fecha']
            hora = request.POST['hora']
            value = modificar_citas(cita_id, paciente, descripcion,
                                    fecha,hora)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'ver_citas', kwargs={'id': request.user.pk}))
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


class HistoriasClinicas(ListView):
    template_name = 'medico/historias_clinicas.html'
    context_object_name = 'historias'

    def get_queryset(self):
        return Historiadetriaje.objects.filter(medico_triaje__usuario__user=self.request.user)


class HistoriasClinicasCrear(View):
    template_name = 'medico/crear_historia.html'

    def get(self, request, *args, **kwargs):
        form = HistoriaClinicaForm(initial={'medico_triaje': Medico.objects.get(usuario__user=request.user)})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('historias_clinicas'))
        else:
            return render_to_response('crear_historia.html', {'form': form},
                                      context_instance=RequestContext(request))


class HistoriasClinicasModificar(UpdateView):
    template_name = 'medico/ver_historia_clinica.html'
    form_class = HistoriaClinicaForm
    success_url = reverse_lazy('historias_clinicas')

    def get_queryset(self):
        return Historiadetriaje.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(
            HistoriasClinicasModificar, self).get_context_data(**kwargs)
        historia = Historiadetriaje.objects.get(pk=self.kwargs['pk'])
        form = HistoriaClinicaForm(
            initial={'medico_triaje': historia.medico_triaje,
                     'paciente': historia.paciente,
                     'antecedentes_personales': historia.antecedentes_personales,
                     'antecedentes_familiares': historia.antecedentes_familiares,
                     'motivo_consulta': historia.motivo_consulta,
                     'enfermedad_actual': historia.enfermedad_actual,
                     'peso': historia.peso,
                     'talla': historia.talla,
                     'signos_vitales': historia.signos_vitales,
                     'piel': historia.piel,
                     'ojos': historia.ojos,
                     'fosas_nasales': historia.fosas_nasales,
                     'conductos_auditivos': historia.conductos_auditivos,
                     'cavidad_oral': historia.cavidad_oral,
                     'cuello': historia.cuello,
                     'columna': historia.columna,
                     'torax': historia.torax,
                     'abdomen': historia.abdomen,
                     'extremidades': historia.extremidades,
                     'genitales': historia.genitales
                     }
        )

        context['form'] = form
        context['historia'] = historia

        return context


class Consultas(TemplateView):
    template_name = 'medico/consulta.html'
    form = Medico_ConsultasForm

    def get_context_data(self, **kwargs):
        context = super(
            Consultas, self).get_context_data(**kwargs)

        cita = Medico_Citas.objects.get(id=self.kwargs['id'])
        id_paciente = cita.paciente

        paciente = Paciente.objects.get(cedula = id_paciente.cedula)
        usuario= Usuario.objects.get(ci=paciente.cedula)
        if cita.es_referido == True:
            referencia = Referencia.objects.get(fecha = cita.fecha,
                                                paciente=cita.paciente_id,
                                                medico = cita.medico,
                                                hora = cita.hora,
                                                descripcion = cita.descripcion)
            context['referencia'] = referencia
        context['consulta'] = cita
        context['cita'] = cita
        context['paciente'] = usuario

        return context


class ComenzarRevision(CreateView):
    template_name = 'medico/comenzar_revision.html'
    form_class = Medico_RevisionForm

    def get_context_data(self, **kwargs):
        context = super(
            ComenzarRevision, self).get_context_data(**kwargs)

        cita = Medico_Citas.objects.get(id=self.kwargs['id'])

        context['consulta'] = cita
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        print("antes de form")
        form = Medico_RevisionForm(request.POST)
        form.fields['otros'].required = False
        print("despues de form")
        if form.is_valid():
            cita = kwargs['id']
            motivos = request.POST['motivos']
            sintomas = request.POST['sintomas']
            presion_sanguinea_diastolica = request.POST['presion_sanguinea_diastolica']
            presion_sanguinea_sistolica = request.POST['presion_sanguinea_sistolica']
            temperatura = request.POST['temperatura']
            frec_respiratoria = request.POST['frec_respiratoria']
            frec_cardiaca = request.POST['frec_cardiaca']
            otros = request.POST['otros']
            value = comenzar_revision(cita, motivos, sintomas, presion_sanguinea_diastolica,
                                    presion_sanguinea_sistolica,temperatura, frec_respiratoria, frec_cardiaca,
                                     otros)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'consulta', kwargs={'id': kwargs['id']}))
            else:
                return render_to_response('medico/comenzar_revision.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(request))
        else:
            cita = Medico_Citas.objects.get(id=self.kwargs['id'])
            messages.error(request,"Por favor verifique los campos siguientes:")
            return render_to_response('medico/comenzar_revision.html',
                                      {'form': form,
                                       'title': 'Agregar',
                                       'consulta':cita},
                                      context_instance=RequestContext(request))


class InformeMedico(CreateView):
    template_name = 'medico/informe_medico.html'
    form_class = Medico_InformeForm
    def get_context_data(self, **kwargs):

        context = super(
            InformeMedico, self).get_context_data(**kwargs)

        cita = Medico_Citas.objects.get(id=self.kwargs['id'])
        fechaNacimiento = cita.paciente.fecha_nacimiento
        sexo = cita.paciente.sexo
        estadoCivil = cita.paciente.estado_civil
        revision = Medico_Revision.objects.get(cita_id=cita.id)

        if fechaNacimiento == None or fechaNacimiento == "None"  :
            fechaNacimiento = '*Información no disponible*'
        else:
            fechaNacimiento = False

        if sexo == None or sexo == "None":
            sexo = '*Información no disponible*'
        else:
            sexo = False
        print(sexo)

        if estadoCivil == None or estadoCivil == "None":
            estadoCivil = '*Información no disponible*'
        else:
            estadoCivil = False

        context['fecha'] = fechaNacimiento
        context['sexo'] = sexo
        context['estado'] = estadoCivil

        context['consulta'] = cita
        context['revision'] = revision
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_InformeForm(request.POST)
        if form.is_valid():
            cita = kwargs['id']
            revision = Medico_Revision.objects.get(pk=cita)
            desc_prediagnostico = request.POST['desc_prediagnostico']
            recipe = request.POST['recipe_medico']
            value = informe_medico(revision.pk, desc_prediagnostico, recipe)
            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'consulta', kwargs={'id': kwargs['id']}))
            else:
                return render_to_response('medico/informe_medico.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/informe_medico.html',
                                      {'form': form,
                                       'title': 'Agregar'},
                                      context_instance=RequestContext(request))


class MyPDFView(DetailView):


    def get(self, request, *args, **kwargs):

        cita = Medico_Citas.objects.get(id=self.kwargs['id'])
        fechaNacimiento = cita.paciente.fecha_nacimiento
        sexo = cita.paciente.sexo
        estadoCivil = cita.paciente.estado_civil

        if fechaNacimiento == None or fechaNacimiento == "None"  :
            fechaNacimiento = '*Información no disponible*'
        if sexo == None or sexo == "None":
            sexo = '*Información no disponible*'
        if estadoCivil == None or estadoCivil == "None":
            estadoCivil = '*Información no disponible*'
        revision = Medico_Revision.objects.get(pk=cita)
        informe = Medico_Informe.objects.get(medico_Revision=revision.pk)
        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        pdf_name = "InformeMedico.pdf"
        response['Content-Disposition'] = 'attachment; filename=InformeMedico.pdf'
        buff = BytesIO()
        # Create the PDF object, using the response object as its "file."
        #p = canvas.Canvas(response)

        doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=20,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )

        elementos = []
        #Definimos los estilos para el documento
        estilo = getSampleStyleSheet()
        estilo_tabla = estilo["BodyText"]
        estilo_tabla.alignment = TA_LEFT
        estilo_tabla.fontName = "Helvetica"
        estilo_tabla.fontSize = 12
        estilo_tabla.leading = 15

        estilo_titulo = estilo["Normal"]
        estilo_titulo.alignment = TA_CENTER
        estilo_titulo.fontName = "Helvetica"
        estilo_titulo.fontSize = 15
        estilo_titulo.leading = 25

        estilo_fecha = estilo["BodyText"]
        estilo_fecha.alignment = TA_RIGHT
        estilo_fecha.fontName = "Helvetica"
        estilo_fecha.fontSize = 10
        estilo_fecha.leading = 25

        elementos.append(Paragraph('Fecha: ' + str(cita.fecha), estilo_fecha))
        elementos.append(Paragraph('INFORME MÉDICO', estilo_titulo))


        data = [
        [''],
        [''],
        [''],
        ['', Paragraph('<b>Institución Médica: </b> ', estilo_tabla),Paragraph(str(cita.institucion.name),
        estilo_tabla), ''],
        ['', Paragraph('<b> CI del Médico Tratante: </b> ', estilo_tabla), Paragraph(str(cita.medico.cedula), estilo_tabla),''],
        ['', Paragraph('<b> Médico Tratante: </b> ', estilo_tabla), Paragraph(str(cita.medico.first_name)+" " + str(cita.medico.last_name), estilo_tabla),''],
        ['', Paragraph('<b> CI del Paciente: </b> ', estilo_tabla), Paragraph(str(cita.paciente.cedula), estilo_tabla),''],
        ['', Paragraph('<b> Nombre del Paciente: </b> ', estilo_tabla), Paragraph(str(cita.paciente.first_name) +" "+str(cita.paciente.last_name ), estilo_tabla),''],
        ['', Paragraph('<b> Fecha de Nacimiento: </b> ', estilo_tabla), Paragraph(str(fechaNacimiento),estilo_tabla),''],
        ['', Paragraph('<b> Sexo: </b> ', estilo_tabla), Paragraph(str(sexo), estilo_tabla),''],
        ['', Paragraph('<b> Estado Civil: </b> ', estilo_tabla), Paragraph(str(estadoCivil),estilo_tabla),''],
        ['', Paragraph('<b> Motivo de la Consulta: </b> ', estilo_tabla), Paragraph(str(revision.motivos), estilo_tabla),''],
        ['', Paragraph('<b> Diagnóstico: </b> ', estilo_tabla), Paragraph(str(informe.desc_prediagnostico),estilo_tabla),''],
        ['', Paragraph('<b> Récipe Médico: </b> ', estilo_tabla), Paragraph(str(informe.recipe_medico),estilo_tabla),'']
        ]

        t = Table(data )
        # t.setStyle(TableStyle([('VALIGN',(1,0),(1,8),'MIDDLE')]))
        t.setStyle(TableStyle(
            [
        ('GRID', (5, 11), (8, -9), 1, colors.dodgerblue),
        ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue)
            ]
        ))

        elementos.append(t)
        #Construimos el documento
        doc.build(elementos)
        response.write(buff.getvalue())
        buff.close()
        return response


class ReferirPaciente(CreateView):

    template_name = 'medico/referir_paciente.html'
    form_class = ReferenciaForm

    def get_context_data(self, **kwargs):

        context = super(
        ReferirPaciente, self).get_context_data(**kwargs)
        cita = Medico_Citas.objects.get(id=self.kwargs['id'])

        context['consulta'] = cita
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = ReferenciaForm(request.POST,request.FILES,cita=kwargs['id'])
        print(form.is_valid())
        if form.is_valid() :
            print("aqui?????")
            id_cita = kwargs['id']
            cita = Medico_Citas.objects.get(id=id_cita)

            archivo = request.FILES['archivo']

            paciente = Paciente.objects.get(cedula = cita.paciente.cedula)

            id_institucion = request.POST['institucion']
            institucion = Institucion.objects.get(id=id_institucion)
            medico = request.POST['medico']
            medico1=Medico.objects.get(cedula = medico)
            usuarioMedico = Usuario.objects.get(id = medico1.usuario_id )
            user_pk = User.objects.get(pk = usuarioMedico.user_id)
            print("supuesto medico")
            print(usuarioMedico.user_id)
            fecha = request.POST['fecha']
            hora = request.POST['hora']
            descripcion = request.POST['descripcion']
            name_especialidad = request.POST['especialidad']
            especialidad = Especialidad.objects.get(nombre_especialidad=name_especialidad)
            subirInforme = Referencia(cita=cita, archivo=archivo,paciente=paciente,
                                medico=medico1, institucion=institucion,
                                descripcion= descripcion, fecha= fecha,
                                hora= hora, especialidad= especialidad)
            subirInforme.save()

            new_cita = agregar_citas(user_pk.id, paciente.cedula, id_institucion, descripcion,
                                   fecha, hora, name_especialidad, es_referido=True)

            if new_cita is True:
                return HttpResponseRedirect(reverse_lazy(
                    'consulta', kwargs={'id': kwargs['id']}))
            else:
                return render_to_response('medico/referir_paciente.html',
                                          {'form': form,
                                           'title': 'Agregar'},
                                          context_instance=RequestContext(request))

        else:
            messages.error(request,"Por favor verifique los campos siguientes:")
            cita = Medico_Citas.objects.get(id=self.kwargs['id'])
            return render_to_response('medico/referir_paciente.html',
                                      {'form': form,
                                      'title': 'Agregar',
                                      'consulta':cita},
                                      context_instance=RequestContext(request))


class VerHistorial(TemplateView):

    template_name = 'medico/ver_historial.html'
    form_class = Medico_HistorialForm

    def get_context_data(self, **kwargs):
        context = super(
            VerHistorial, self).get_context_data(**kwargs)
        consulta = Medico_Citas.objects.get(pk=self.kwargs['id'])
        paciente = consulta.paciente
        historial = Medico_Citas.objects.filter(
            paciente=paciente).order_by('fecha')

        context['historial'] = historial
        context['consulta'] = consulta

        return context
