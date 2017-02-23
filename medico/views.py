#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth import *
from django.contrib import messages
from django.views.generic import *
from administrador.forms import *
from medico.forms import *
from medico.models import *
from medico.controllers import *
from administrador.models import *
import datetime
import calendar
import parsedatetime as pdt


class PerfilMedico(CreateView):
    template_name = 'medico/perfil_medico.html'
    form_class = UsuarioForm

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
                            direccion='', usuario=usuario)
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
        form = UsuarioForm(request.POST)
        form.fields['username'].required = False
        form.fields['passw'].required = False
        form.fields['ci'].required = False
        form.fields['rol'].required = False
        if form.is_valid():
            nombre = request.POST['first_name']
            apellido = request.POST['last_name']
            email = request.POST['email']
            sexo = request.POST['sex']
            fecha = request.POST['birth_date']
            estado_civil = request.POST['marital_status']
            telefono = request.POST['phone']
            direccion = request.POST['address']
            value = editar_medico(request.user, nombre, apellido, email, sexo,
                                  fecha, estado_civil, telefono, direccion)

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


class AgregarConsulta(TemplateView):
    template_name = 'medico/agregar_consulta.html'


class BuscarPaciente(TemplateView):
    template_name = 'medico/buscar.html'

    def get_context_data(self, **kwargs):
        context = super(
            BuscarPaciente, self).get_context_data(**kwargs)

        pacientes = Paciente.objects.all()

        context['result'] = pacientes

        return context


class BuscarMedico(TemplateView):
    template_name = 'medico/buscar.html'

    def get_context_data(self, **kwargs):
        context = super(
            BuscarMedico, self).get_context_data(**kwargs)

        pacientes = Medico.objects.all()

        context['result'] = pacientes

        return context


class VerCitas(TemplateView):
    template_name = 'medico/ver_citas.html'

    def get_context_data(self, **kwargs):
        context = super(
            VerCitas, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['id'])
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
        form = Medico_CitasForm(request.POST)
        if form.is_valid():
            user_pk = request.user.pk
            paciente = request.POST['paciente']
            institucion = request.POST['institucion']
            fecha = request.POST['fecha']
            descripcion = request.POST['descripcion']
            value = agregar_citas(user_pk, paciente, institucion, descripcion,
                                  fecha)
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
            messages.error(request,"Por favor verifique que los campos estan en color rojo.")
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
                'institucion': cita.institucion
                }
        form = Medico_CitasForm(initial=data)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = Medico_CitasForm(request.POST)
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
        cita = Medico_Citas.objects.get(paciente=self.kwargs['id'])
        context['paciente'] = cita
        return context
