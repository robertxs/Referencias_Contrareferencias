from administrador.models import *
from paciente.models import *
from medico.models import *
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def register_user(form):
    # Almacenamos el usuario
    save_user = form.save()
    # Agregamos al usuario al grupo de acuerdo al rol
    user = User.objects.get(username=save_user.username)
    usuario = Usuario(user=user, ci=form.cleaned_data['ci'])
    usuario.save()
    group = Group.objects.get(name=form.cleaned_data['rol'])
    user.groups.add(group)
    if form.cleaned_data['rol'] == 'paciente':
        paciente = Paciente(cedula=usuario.ci, usuario=usuario,
                            first_name=user.first_name,
                            last_name=user.last_name)
        paciente.save()
    elif form.cleaned_data['rol'] == 'medico':
        medico = Medico(cedula=usuario.ci, usuario=usuario,
                        first_name=user.first_name,
                        last_name=user.last_name)
        medico.save()
    return user


def modificar_usuario(usuario_id, username, first_name,
                      last_name, email, rol):
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
        user = User.objects.get(pk=usuario.user.pk)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        group = Group.objects.get(name=rol)
        user.groups.remove(usuario.user.groups.all()[0])
        user.groups.add(group)
        usuario.save()
        user.save()
        return True
    except:
        return False


def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    user = User.objects.get(pk=usuario.user.pk)
    usuario.delete()
    user.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_usuarios'))


def agregar_rol(name):
    try:
        group = Group(name=name)
        group.save()
        return True
    except:
        return False


def eliminar_rol(request,pk):
    rol = Group.objects.get(pk=pk)
    if (rol.name == 'admin') or (rol.name == 'medico') or (rol.name == 'paciente'):
        messages.error(request,"No se puede eliminar este rol.")
    else :
        rol.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_roles'))


def agregar_institucion(rif, nombre, direccion,tipo):
    try:
        institucion = Institucion(rif=rif,
                            name = nombre,
                            address =direccion,
                            tipo = tipo)
        institucion.save()
        return True
    except:
        return False


def modificar_institucion(inst_id, direccion, tipo):
    try:
        institucion = Institucion.objects.get(pk=inst_id)
        institucion.address = direccion
        institucion.tipo = tipo
        institucion.save()
        return True
    except:
        return False


def eliminar_institucion(request, pk):
    institucion = Institucion.objects.get(pk=pk)
    institucion.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_instituciones'))


def agregar_especialidad(nombre):
    try:
        especialidad = Especialidad(nombre_especialidad = nombre)
        especialidad.save()
        return True
    except:
        return False


def modificar_especialidad(anterior, nombre):
    try:
        especialidad = Especialidad.objects.get(nombre_especialidad=anterior)
        especialidad.delete()
        especialidad = Especialidad(nombre_especialidad = nombre)
        especialidad.save()
        return True
    except:
        return False

def eliminar_especialidad(request, pk):
    especialidad = Especialidad.objects.get(pk=pk)
    especialidad.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_especialidades'))
